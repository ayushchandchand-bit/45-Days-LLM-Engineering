# 01 — System Prompts

A chat request is a list of **messages**, each with a `role`. The first one can be a special
`system` message: it sets **who the assistant is and how it must behave** — before the user ever
speaks.

```python
messages = [
    {"role": "system", "content": "You are a terse expert. Answer in one sentence."},
    {"role": "user",   "content": "What is recursion?"},
]
```

## What the three roles mean
| Role | Who | Use it for |
|------|-----|------------|
| `system` | the rules | persona, tone, format, hard constraints ("only JSON", "never guess") |
| `user` | you | the actual question or task |
| `assistant` | the model | its replies (and, in few-shot, *example* replies — module 03) |

## Why it matters
The system prompt is your **steering wheel**. The same model + same question gives a one-line expert
answer, a friendly analogy, or strict JSON — purely based on the system message. Set behaviour
**once** in `system`, then keep each `user` message focused on the task.

## Good system-prompt ingredients
- **Role:** "You are a senior Python reviewer."
- **Audience:** "Explain for a first-year B.Tech student."
- **Format:** "Reply in at most 3 bullet points." / "Reply only with JSON."
- **Guardrails:** "If you are unsure, say 'I don't know' — never invent facts."

Run it to see one question answered three ways (needs `GROQ_API_KEY`):

```bash
python system_prompts.py
```

➡ Next: [02-zero-shot](../02-zero-shot/)
