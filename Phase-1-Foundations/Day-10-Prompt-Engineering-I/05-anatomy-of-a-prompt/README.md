# 05 — Anatomy of a Prompt (Putting It Together)

The four techniques aren't rivals — they **stack**. A reliable prompt usually has all of these:

```text
ROLE        (system)     "You are a senior support agent."
TASK        (zero-shot)  "Classify the message. Reply with one of: ORDER, REFUND, DELIVERY, OTHER."
EXAMPLES    (few-shot)   a couple of input -> output pairs
REASONING   (CoT)        "Think step by step." (only if the task needs it)
FORMAT      (always)     "Reply with one word." / "Reply only with JSON."
```

## The 5-point checklist
| # | Piece | Ask yourself |
|--:|-------|--------------|
| 1 | **Role** | Who should the model *be*? (system message) |
| 2 | **Task** | What exactly to do, and what are the allowed answers? |
| 3 | **Examples** | Does format/edge-case handling need a few demos? |
| 4 | **Reasoning** | Is this multi-step? Then let it think first. |
| 5 | **Format** | Is the output shaped so my *code* can use it? |

## Start small, then add
Don't write a giant prompt on day one. Start zero-shot. If it's unreliable, add the missing piece:
- wrong *vocabulary/format* → add **examples**
- wrong *answers on hard inputs* → add **chain-of-thought**
- inconsistent *persona/tone* → strengthen the **system** message

> Prompt engineering is **iteration**, not magic words. Change one thing, re-run, compare.

This module's script assembles a prompt from the four pieces and prints the message list — **no API
key needed**, it just shows the structure:

```bash
python prompt_builder.py
```

➡ Next: practise in [../exercises/](../exercises/)
