# 01 — Your First Groq Call

Time to talk to a real LLM. We'll use **Groq** — it serves open models (Llama and friends) on very
fast hardware and has a generous **free tier**, so it's perfect for learning.

## Three steps
1. **Create a client** with your key (from `.env`, never hardcoded).
2. **Pick a model** — `llama-3.1-8b-instant` is fast and free.
3. **Generate** — send a list of messages, read the reply.

```python
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Explain what an API is in one sentence."}],
)
print(response.choices[0].message.content)
```

> **Why `messages` (a list) instead of one string?** Chat models think in **turns**, each with a
> `role`: `"user"` (you), `"assistant"` (the model), and an optional `"system"` (instructions). This
> is the same shape OpenAI uses — learn it once, reuse it everywhere.

## What you get back
`response.choices[0].message.content` is the model's answer as a string. The full `response` also
carries metadata — `response.usage` (token counts) and a finish reason — which you'll use later.

| You send | You get |
|----------|---------|
| `messages` (list of turns) | `response.choices[0].message.content` (the answer) |
| | `response.usage` (`prompt_tokens`, `completion_tokens`, `total_tokens`) |

## Get a free key
1. Sign in at **[console.groq.com](https://console.groq.com)**.
2. Create an API key under **[API Keys](https://console.groq.com/keys)**.
3. Put it in a `.env` file: `GROQ_API_KEY=your_key_here` (never commit it).

## Gotchas
- Model names change over time. If `llama-3.1-8b-instant` isn't available, check the current free
  models at [console.groq.com/docs/models](https://console.groq.com/docs/models).
- Free tiers have **rate limits** (requests/tokens per minute). You'll handle those on Day 14.

Run it (needs `GROQ_API_KEY` in `.env`):

```bash
python first_call.py
```

➡ Next: [02-tokens-and-tokenization](../02-tokens-and-tokenization/)
