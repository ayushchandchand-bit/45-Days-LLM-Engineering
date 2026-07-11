# 03 · LCEL — Chaining with `|`

This is the idea the whole framework is built on. **LCEL** ("LangChain Expression Language")
sounds fancy but it's one rule:

> The `|` operator feeds the output of the thing on its **left** into the thing on its **right**.

```python
chain = prompt | model | parser
```

Read left to right: **fill the prompt → send it to the model → pull clean text out of the reply.**

## `|` is just data flowing left → right

You can see it with two plain functions — no model needed:
```python
from langchain_core.runnables import RunnableLambda

to_upper = RunnableLambda(lambda s: s.upper())
add_bang = RunnableLambda(lambda s: s + "!")

tiny = to_upper | add_bang
tiny.invoke("hello")     # -> "HELLO!"
```
`RunnableLambda` wraps any function so it can join a chain. That's the entire trick behind `|`.

## The real chain

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer in one short sentence."),
    ("human", "{question}"),
])
parser = StrOutputParser()
model  = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

chain = prompt | model | parser
chain.invoke({"question": "What is Python?"})   # -> a plain string
```

What each stage receives and returns:

| Stage | Gets | Returns |
|-------|------|---------|
| `prompt` | `{"question": "..."}` (a dict) | a `PromptValue` (the filled messages) |
| `model` | the messages | an `AIMessage` |
| `parser` | the `AIMessage` | a plain `str` (`StrOutputParser` grabs `.content`) |

Without the parser the chain would hand you an `AIMessage`; with it you get a clean string —
usually what you want.

## One interface: `invoke` / `batch` / `stream`

The chain is itself a **Runnable**, so it has the same three methods every piece has:

| Method | Does | Use when |
|--------|------|----------|
| `.invoke(x)` | one input → one output | the normal case |
| `.batch([x, y, z])` | many inputs at once (parallel) | processing a list fast |
| `.stream(x)` | yields the answer piece by piece | live "typing" UIs (Day 19) |

Because *every* component — prompt, model, parser, retriever, tool — is a Runnable, they all
share these methods and all snap together with `|`. Learn the interface once; it's the same everywhere.

## Why this replaced the old way

Older tutorials use `LLMChain`, `SequentialChain`, etc. LCEL made those obsolete: `|` composition
gives you batching, streaming, and async **for free**, with far less code. If you see `LLMChain`
in a blog post, it's pre-2024 — use `prompt | model | parser` instead.

## Run it

```bash
python lcel_chains.py
```
Step 1 (the `|` proof) runs with no key; the full chain, `batch`, and `stream` run with a key.

➡ Next: [04 · Output Parsers](../04-output-parsers/README.md) — turn replies into typed data.
