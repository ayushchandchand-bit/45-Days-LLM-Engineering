"""
02 - Prompt templates: reusable prompts with fill-in-the-blanks.

Hand-writing the whole message list every time is repetitive and error-prone.
A ChatPromptTemplate is a prompt with {placeholders} you fill in later. Write
the wording once; feed it different values forever.

Most of this file runs WITHOUT a key: turning a template + values into finished
messages is pure local work (no network). We only need Groq for the last part.

Setup:
    pip install langchain langchain-groq python-dotenv
Run:
    python prompt_templates.py
"""

from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

MODEL = "llama-3.1-8b-instant"

# --- 1. Define a template once --------------------------------------------
# from_messages takes (role, text) tuples. Anything in {curly_braces} is a
# variable to be filled in later. Roles: "system", "human", "ai".
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a translator. Translate the text into {language}. Reply with only the translation."),
    ("human", "{text}"),
])

print("Template variables it expects:", prompt.input_variables)  # ['language', 'text']
print()

# --- 2. Fill it in -> finished messages (this is offline!) ----------------
# .format_messages(...) substitutes the values and returns real message objects,
# exactly what a model expects. Great for *seeing* your prompt before sending it.
messages = prompt.format_messages(language="French", text="Good morning, friends!")

print("After filling language='French', text='Good morning, friends!':")
for m in messages:
    print(f"  [{m.type:>6}] {m.content}")
print()

# Reuse the SAME template with different values -- no rewriting:
messages_hi = prompt.format_messages(language="Hindi", text="Good morning, friends!")
print("Reused with language='Hindi':")
for m in messages_hi:
    print(f"  [{m.type:>6}] {m.content}")
print()

# --- 3. Why not just an f-string? -----------------------------------------
# f-strings glue text together but know nothing about *roles*. A template keeps
# the system/human structure, validates that you supplied every variable, and
# plugs straight into chains (next module). Try leaving one out:
try:
    prompt.format_messages(language="German")   # forgot 'text'
except KeyError as e:
    print("Missing a variable is caught for you:", e)
print()

# --- 4. Send it to the model (needs a key) --------------------------------
if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY set - skipping the live translation (this is fine).")
else:
    model = ChatGroq(model=MODEL, temperature=0)
    reply = model.invoke(messages)              # 'messages' from step 2 (French)
    print("Model translation (French):", reply.content)
