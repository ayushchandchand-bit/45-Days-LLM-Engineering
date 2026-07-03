# 05 — Model Families: Which One, and Where It Runs

"An LLM" isn't one thing. You'll choose between **sizes**, **providers**, and **hosted vs local**.
For this course, all picks are **free**.

## Size: speed vs smarts (within one provider)
| Tier | Example (Groq) | Good for |
|------|----------------|----------|
| Small / fast | `llama-3.1-8b-instant` | most tasks: fast, cheap, free |
| Large | `llama-3.3-70b-versatile` | hard reasoning, long/complex work |

Start with the **small** model. Reach for the **large** one only when the small isn't good enough —
it's slower and costlier.

## Providers we use (all free)
| Provider | What it is | Why use it |
|----------|------------|------------|
| **Groq** | super-fast hosted open models (Llama, etc.) | our default; fast + generous free tier |
| **Ollama** | runs open models **on your laptop** | offline, private, no key, no limits |
| **Hugging Face** | hosted inference for open models | huge model zoo |
| **Gemini** | Google's hosted models | huge context; Google ecosystem (paid beyond trials) |

## Hosted vs local
- **Hosted (Groq, HF, Gemini):** strong quality, nothing to install, needs internet + a key,
  has rate limits.
- **Local (Ollama):** private and unlimited, but quality/speed depend on your hardware.

## The takeaway
> Default to **Groq's small Llama**. Switch providers/sizes for smarts, privacy, or context —
> and on **Day 12** you'll hide all of them behind **one interface** so swapping is trivial.

This module is concept-only — there's a tiny script that prints a decision cheat-sheet.

```bash
python model_cheatsheet.py
```

➡ Next: practise in [../exercises/](../exercises/)
