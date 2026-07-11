"""
01 - Why LangChain? The same Groq call, wrapped in a common interface.

On Day 9 we called Groq directly with the `groq` client. That works great.
So why add a framework? Because LangChain gives every model provider the SAME
shape: build messages -> `.invoke(messages)` -> get a reply. Swap Groq for
OpenAI/Anthropic/Ollama by changing ONE line, and reuse the same prompts,
chains, parsers, and memory on top.

This file shows the LangChain version of a Day-9 call, side by side in spirit.

Setup:
    pip install langchain langchain-groq python-dotenv
    # put GROQ_API_KEY=... in a .env file (free key at console.groq.com/keys)
Run:
    python why_langchain.py

Runs offline too: with no key it still shows how messages are built, then
skips only the live network call.
"""

from dotenv import load_dotenv
import os

# LangChain represents a chat turn as a typed *message object*, not a dict.
# (Day 9 used {"role": "user", "content": "..."}; same idea, nicer type.)
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

load_dotenv()

MODEL = "llama-3.1-8b-instant"   # fast + free on Groq

# --- 1. Build the conversation as message OBJECTS -------------------------
# Each class carries a role. This list is the LangChain equivalent of the
# list-of-dicts we sent on Day 9.
messages = [
    SystemMessage("You are a concise assistant. Answer in one sentence."),
    HumanMessage("Explain what an API is."),
]

print("The messages we will send (role -> text):")
for m in messages:
    # .type is 'system' / 'human' / 'ai' -- the role, in LangChain's words.
    print(f"  [{m.type:>6}] {m.content}")
print()

# --- 2. The live call (only if a key is present) --------------------------
if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY set - skipping the live call (this is fine).")
    print("Add a key to .env to see the real answer.")
else:
    # ChatGroq is the LangChain wrapper around the Groq client.
    # temperature=0 -> deterministic, good for demos.
    model = ChatGroq(model=MODEL, temperature=0)

    # .invoke() takes the messages and returns ONE AIMessage back.
    reply = model.invoke(messages)

    print("Reply type:", type(reply).__name__)   # AIMessage
    print("Answer    :", reply.content)

    # The reply also carries metadata (token usage, model name, etc.).
    usage = reply.usage_metadata
    if usage:
        print("Tokens    :", usage)   # {'input_tokens': .., 'output_tokens': .., ..}

# --- 3. The whole point: swapping providers is a one-line change ----------
print()
print("Why bother with the wrapper? To switch providers you change ONE line:")
print('  Groq    :  model = ChatGroq(model="llama-3.1-8b-instant")')
print('  OpenAI  :  model = ChatOpenAI(model="gpt-4o-mini")')
print('  Ollama  :  model = ChatOllama(model="llama3.1")   # 100% local')
print("Everything built on top -- prompts, chains, parsers, memory -- stays the same.")
