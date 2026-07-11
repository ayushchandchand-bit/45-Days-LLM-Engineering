# 01 · Why LangChain?

We already called Groq directly on **Day 9**. It worked. So why learn a framework?

> **LangChain gives every LLM provider the same shape.** Build messages → `.invoke()` →
> get a reply. Then reuse the *same* prompts, chains, parsers, and memory on top of any model.

## The two calls, side by side

**Day 9 — raw Groq client:**
```python
from groq import Groq
client = Groq()
resp = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Explain what an API is."}],
)
print(resp.choices[0].message.content)
```

**Day 21 — LangChain:**
```python
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
reply = model.invoke([HumanMessage("Explain what an API is.")])
print(reply.content)
```

Same call, tidier surface. The payoff isn't *this one line* — it's everything that clicks
onto `.invoke()` later (templates, `|` chains, parsers, memory, tools, agents).

## Messages are objects now, not dicts

| Day 9 (dict)                                   | Day 21 (object)                  | Role     |
|------------------------------------------------|----------------------------------|----------|
| `{"role": "system", "content": "..."}`         | `SystemMessage("...")`           | instructions |
| `{"role": "user", "content": "..."}`           | `HumanMessage("...")`            | the user |
| `{"role": "assistant", "content": "..."}`      | `AIMessage("...")`               | the model |

`model.invoke(messages)` returns **one `AIMessage`** — read the text with `reply.content`,
and token counts with `reply.usage_metadata`.

## The real reason: swap providers in one line

```python
model = ChatGroq(model="llama-3.1-8b-instant")   # free + fast (our default)
model = ChatOpenAI(model="gpt-4o-mini")          # OpenAI
model = ChatOllama(model="llama3.1")             # 100% local, no key
```

Every prompt, chain, and parser you build this week sits **on top** of that one object,
so switching models never touches the rest of your app.

## The install

```bash
pip install langchain langchain-groq
```
- `langchain-core` — the base pieces (messages, prompts, runnables) — pulled in automatically.
- `langchain-groq` — the Groq integration (`ChatGroq`). Each provider ships its own small package.

## Run it

```bash
python why_langchain.py
```
With no `GROQ_API_KEY` it still prints how the messages are built and skips only the live call.

➡ Next: [02 · Prompt Templates](../02-prompt-templates/README.md) — stop hand-writing prompts.
