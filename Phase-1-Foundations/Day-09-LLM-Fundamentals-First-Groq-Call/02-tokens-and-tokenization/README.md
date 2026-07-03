# 02 — Tokens & Tokenization

LLMs don't read words or letters — they read **tokens**. A token is a chunk of text, often a word
or part of a word. Roughly: **1 token ≈ 4 characters ≈ ¾ of a word** in English.

```text
"I love samosas"  ->  ["I", " love", " samos", "as"]   (about 4 tokens)
```

Why you must care:
| Tokens decide… | Because |
|----------------|---------|
| **Cost** | APIs bill per token (in + out) |
| **Limits** | the context window is measured in tokens |
| **Speed** | more tokens = slower responses |

## Counting tokens with Groq
Groq has no separate "count only" endpoint — but **every response reports its token usage**. So we
send the text with `max_tokens=1` (ask for the tiniest reply) just to read `usage.prompt_tokens`:

```python
client = Groq(api_key=os.environ["GROQ_API_KEY"])
resp = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "How many tokens is this?"}],
    max_tokens=1,
)
print(resp.usage.prompt_tokens)
```

> **Read the trend, not the exact number.** `prompt_tokens` counts your text *plus* a few tokens of
> chat scaffolding (the role markers), so short strings look a little inflated by a fixed amount.
> What matters is how the count **grows** with longer, rarer, or non-English text.

## Things that surprise beginners
- **Spaces and punctuation** are part of tokens too.
- **Non-English** text (e.g. Hindi in Devanagari) often uses **more** tokens per word.
- Numbers and code can tokenize oddly — never assume "1 word = 1 token".

Run it (needs `GROQ_API_KEY`):

```bash
python count_tokens.py
```

➡ Next: [03-context-windows](../03-context-windows/)
