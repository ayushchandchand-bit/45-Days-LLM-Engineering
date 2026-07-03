# 03 — Few-Shot Prompting

**Few-shot** = you put a few **worked examples** in the prompt before the real question. The model
copies the *pattern* it sees — your exact labels, your exact format — instead of guessing.

"Shot" = one example. Zero-shot = 0 examples, few-shot = a handful (2–5 is usually plenty).

## How you pass examples
Examples are just **fake prior turns**: an example `user` message, then the ideal `assistant` reply,
repeated. The real message goes last.

```python
messages = [
    {"role": "system",    "content": "Reply with only the team name."},
    {"role": "user",      "content": "Where is my package?"},   # example in
    {"role": "assistant", "content": "DELIVERY"},                # example out
    {"role": "user",      "content": "I want my money back."},  # example in
    {"role": "assistant", "content": "REFUND"},                 # example out
    {"role": "user",      "content": "My order never arrived."},# the REAL question
]
```

## When to reach for it
| Situation | Why few-shot helps |
|-----------|--------------------|
| Custom label set (`ORDER/REFUND/DELIVERY/OTHER`) | examples pin the exact vocabulary |
| Strict output format (CSV row, JSON shape) | the model mimics the shape precisely |
| Subtle style/tone | "show, don't tell" beats describing it |

## Tips
- **Cover the variety** — include a tricky/edge example, not just easy ones.
- **Be consistent** — your examples must follow the rule perfectly; mistakes get copied.
- **Keep it lean** — more examples = more tokens (cost + latency). Stop when it's reliable.

Run it to watch labels snap into place once examples are added (needs `GROQ_API_KEY`):

```bash
python few_shot.py
```

➡ Next: [04-chain-of-thought](../04-chain-of-thought/)
