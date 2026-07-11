"""
03 - LCEL: chaining pieces with the | operator (the core idea of LangChain).

LCEL = "LangChain Expression Language". It's just this: the pipe operator |
feeds the output of the thing on its left into the thing on its right.

    chain = prompt | model | parser

Read it left to right: fill the prompt -> send to the model -> pull clean text
out of the reply. The whole chain is itself a "Runnable" with .invoke(),
.batch(), and .stream().

The | mechanics run offline (we chain two plain Python functions to prove it).
The full prompt|model|parser needs a key.

Setup:
    pip install langchain langchain-groq python-dotenv
Run:
    python lcel_chains.py
"""

from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq

load_dotenv()

MODEL = "llama-3.1-8b-instant"

# --- 1. What | actually does (offline proof) ------------------------------
# RunnableLambda wraps any plain function so it can join a chain. Piping two
# of them means: output of the first becomes input to the second.
to_upper = RunnableLambda(lambda s: s.upper())
add_bang = RunnableLambda(lambda s: s + "!")

tiny_chain = to_upper | add_bang            # "feed left's output into right"
print("tiny_chain.invoke('hello') =>", tiny_chain.invoke("hello"))   # HELLO!
print("The | is just data flowing left -> right. That's all LCEL is.")
print()

# --- 2. The real chain: prompt | model | parser ---------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer in one short sentence."),
    ("human", "{question}"),
])

# StrOutputParser pulls the plain-text .content OUT of the AIMessage, so the
# chain returns a clean string instead of a message object.
parser = StrOutputParser()

# You need a model object to build the full chain; construct it only if we can.
if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY set - skipping the live prompt|model|parser chain.")
    print("With a key, this runs:")
    print('    chain = prompt | model | parser')
    print('    chain.invoke({"question": "What is Python?"})  ->  a plain string')
else:
    model = ChatGroq(model=MODEL, temperature=0)
    chain = prompt | model | parser         # <-- the whole app in one line

    # 2a. invoke: one input -> one answer.
    answer = chain.invoke({"question": "What is Python, in one line?"})
    print("invoke ->", answer)
    print()

    # 2b. batch: many inputs at once (runs them in parallel under the hood).
    questions = [
        {"question": "What is HTML?"},
        {"question": "What is HTTP?"},
    ]
    for q, a in zip(questions, chain.batch(questions)):
        print(f"batch -> {q['question']:12} {a}")
    print()

    # 2c. stream: get the answer piece by piece as it's generated.
    print("stream -> ", end="", flush=True)
    for piece in chain.stream({"question": "Name three uses of Python."}):
        print(piece, end="", flush=True)
    print()

# --- 3. The takeaway ------------------------------------------------------
print()
print("Every LangChain piece (prompt, model, parser, retriever, tool) is a")
print("Runnable, so they all share invoke/batch/stream and all snap together with |.")
