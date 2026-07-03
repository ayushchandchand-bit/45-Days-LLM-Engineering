# 05 — Gemini Embeddings (Optional Cloud Provider)

Everything so far ran **locally** for free — that's our default and it's enough for the whole course.
This module shows the **same idea from a cloud API** (Google Gemini) so you know how a hosted
embedding provider looks. **It's optional** and needs a free API key.

## Local vs cloud — when would you use cloud?
| | Local (`sentence-transformers`) | Cloud (Gemini) |
|--|--|--|
| Cost | free | free tier, then paid |
| Setup | `pip install`, one-time model download | API key, internet every call |
| Privacy | text never leaves your machine | text sent to Google |
| Vector size | 384 (MiniLM) | 768–3072 (configurable) |
| Best when | learning, prototypes, private data | you want top quality / no local compute |

The **code shape is identical** — text in, vector out, cosine to compare. Only the line that produces
the vector changes. That's the real lesson: providers are swappable.

## The call (google-genai SDK)
```python
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents="I love learning about AI",
)
vector = result.embeddings[0].values     # a list of floats
```

## Setup (only if you want to run this one)
```bash
pip install google-genai            # already in requirements.txt
```
Get a free key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey) and add it to
`.env`:
```bash
# .env  (never commit this)
GEMINI_API_KEY=your_key_here
```

`gemini_embeddings.py` is written to **fail gracefully**: with no key it prints a friendly note and
exits, so the rest of the day still runs without one.

> **Takeaway:** the provider is an implementation detail. Pick local for free + private; pick a cloud
> API when you want a bigger/stronger model and don't mind sending text out. The retrieval math
> (cosine, nearest-neighbour) is exactly the same either way.

Run it (optional — needs `GEMINI_API_KEY`):
```bash
python gemini_embeddings.py
```

➡ Back to the [Day 17 README](../README.md) · then try the [exercises](../exercises/).
