# 02 — Zero-Shot Prompting

**Zero-shot** = you ask the model to do a task **with no examples** — instructions only. Modern
models are trained on so much text that for common tasks (classify, summarise, translate, extract),
a clear instruction is often all you need.

The catch: *clear* is doing a lot of work. Vague in → vague out.

## Vague vs crisp
| Vague ❌ | Crisp ✅ |
|---------|---------|
| "Tell me about this review." | "Classify sentiment. Reply with exactly one word: Positive, Negative, or Neutral." |
| "Summarise this." | "Summarise in 2 bullet points, max 15 words each." |
| "Is this email urgent?" | "Reply only `yes` or `no`: does this email need a reply within 24 hours?" |

## The crisp-instruction recipe
1. **The task** — "Classify the sentiment of the review."
2. **The allowed outputs** — "one of: Positive, Negative, Neutral."
3. **The format** — "Reply with exactly one word. No other text."

Constraining the output is what makes the result **usable by your code** (you can't `if` on a
paragraph, but you can on `"Positive"`).

## When zero-shot isn't enough
If the model keeps getting the *format* or *edge cases* wrong, don't write a longer essay of rules —
**show it examples** instead. That's few-shot (next module).

Run it to compare a vague prompt with a crisp one (needs `GROQ_API_KEY`):

```bash
python zero_shot.py
```

➡ Next: [03-few-shot](../03-few-shot/)
