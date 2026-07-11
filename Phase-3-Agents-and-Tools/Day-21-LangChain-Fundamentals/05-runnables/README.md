# 05 · Runnables & Composition

A real pipeline isn't always a straight line. Three small helpers cover almost everything you'll
need to branch and recombine — and they're all **pure Python**, so this whole module runs with no key.

## The three glue pieces

| Runnable | What it does | Picture |
|----------|--------------|---------|
| `RunnableLambda(fn)` | wraps any function as a chain step | `x → fn(x)` |
| `RunnableParallel(a=.., b=..)` | runs several steps on the **same** input, returns a dict | `x → {"a": .., "b": ..}` |
| `RunnablePassthrough()` | passes the input through **unchanged** | `x → x` |

```python
analyze = RunnableParallel(
    upper=RunnableLambda(str.upper),
    words=RunnableLambda(lambda s: len(s.split())),
)
analyze.invoke("langchain is fun")
# -> {"upper": "LANGCHAIN IS FUN", "words": 3}
```

`RunnablePassthrough` shines when a later step needs **both** the raw input and something computed
from it:
```python
RunnableParallel(
    original=RunnablePassthrough(),   # keep the input
    shout=RunnableLambda(str.upper),  # and a transformed copy
).invoke("hello")
# -> {"original": "hello", "shout": "HELLO"}
```

## Shortcut: a plain dict *is* a `RunnableParallel`

Inside a chain, LangChain auto-wraps a dict of runnables into a `RunnableParallel`. So you'll
usually just write the dict:
```python
{"context": retriever, "question": RunnablePassthrough()} | prompt | model | parser
```

## This exact shape *is* RAG

That one line is how retrieval-augmented generation is wired — the same load→retrieve→answer flow
you built by hand on Day 20, now as an LCEL chain:

```python
{
    "context":  retriever,              # question -> relevant chunks
    "question": RunnablePassthrough(),  # question -> itself
} | prompt | model | parser
```

The dict fills the prompt's `{context}` and `{question}`; the filled prompt goes to the model; the
parser cleans the reply. The module script builds this **without a model** so you can print the
finished prompt and see the wiring before adding `| model | parser`.

## Why it all composes

Every one of these is a Runnable, so it has `invoke` / `batch` / `stream` and joins with `|`.
Learn `Lambda` / `Parallel` / `Passthrough` and you can assemble most pipelines you'll meet —
including the agent tool-wiring coming later in Phase 3.

## Run it

```bash
python composition.py
```
Runs entirely offline — composition is pure Python.

➡ Next: [06 · Conversation Memory](../06-memory/README.md) — remember the chat, the LangChain way.
