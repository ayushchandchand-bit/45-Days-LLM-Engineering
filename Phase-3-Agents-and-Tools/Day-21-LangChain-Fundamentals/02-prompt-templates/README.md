# 02 · Prompt Templates

Writing the full message list by hand every time gets old fast. A **prompt template** is a
prompt with `{blanks}` you fill in later — write the wording once, feed it new values forever.

## The pattern

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a translator. Translate into {language}. Reply with only the translation."),
    ("human", "{text}"),
])

messages = prompt.format_messages(language="French", text="Good morning, friends!")
```

- `from_messages` takes `(role, text)` tuples. Roles are `"system"`, `"human"`, `"ai"`.
- Anything in `{curly_braces}` is a **variable**. `prompt.input_variables` lists them.
- `.format_messages(**values)` substitutes the values and returns real message objects —
  **no network call**, so you can print and inspect your prompt before ever sending it.

## Template vs. f-string — why bother?

You *could* build the string with an f-string. A template does three things an f-string can't:

| | f-string | `ChatPromptTemplate` |
|--|----------|----------------------|
| Keeps system/human **roles** | ✗ (just text) | ✓ |
| **Checks** you supplied every variable | ✗ | ✓ (errors if one's missing) |
| Plugs into a **chain** with `\|` | ✗ | ✓ (next module) |
| Reuse with new values | copy-paste | one object, call again |

Forget a variable and it tells you, instead of silently sending a broken prompt:
```python
prompt.format_messages(language="German")   # KeyError: 'text'
```

## `format_messages` vs `invoke`

- `prompt.format_messages(...)` → the finished **messages** (for inspecting / passing to a model).
- `prompt.invoke({...})` → a `PromptValue` (what a **chain** passes along — see module 03).

Both fill the same blanks; use `format_messages` when you want to *see* the result.

## Coming up: `MessagesPlaceholder`

A template can also reserve a slot for a whole *list* of past messages —
`MessagesPlaceholder("history")` — which is how we bolt conversation memory onto a prompt in
[module 06](../06-memory/README.md). Noted here; used there.

## Run it

```bash
python prompt_templates.py
```
Steps 1–3 run with no key (pure local formatting); step 4 does the live translation if a key is set.

➡ Next: [03 · LCEL Chains](../03-lcel-chains/README.md) — the `|` operator that ties it all together.
