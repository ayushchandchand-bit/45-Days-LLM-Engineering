# 04 — Chain-of-Thought (CoT)

A model writes one token at a time, left to right. If you demand the final answer **immediately**, it
has to commit before it has "worked anything out." For multi-step problems that's where it slips.

**Chain-of-thought** = ask it to **reason step by step first**, *then* give the answer. Those
intermediate steps act as scratch paper, and accuracy jumps.

```text
Prompt: "Think step by step, then write 'Answer: <number>' on the last line."
```

## Why it works
The reasoning tokens give the model a place to break the problem down — multiply, subtract, check —
before stating a result. It's the difference between blurting and showing your working.

## When to use it (and not)
| Use CoT | Skip CoT |
|---------|----------|
| maths, logic, word problems | a simple fact lookup |
| multi-step planning | a one-word classification |
| "compare A and B, then decide" | format-only transforms |

CoT costs **extra tokens** (it literally writes more), so reserve it for tasks that actually need
reasoning.

## Make the answer parseable
Reasoning is great for accuracy but messy for your code. So **pin the answer to a fixed spot**:

> "On the last line, write `Answer: <number>` and nothing else."

Then your code reads just that line. (Day 11 takes this further with **structured JSON output**.)

## A useful cousin: zero-shot CoT
Just appending **"Let's think step by step."** to a question often triggers the same effect with no
examples needed.

Run it to compare a bare answer with step-by-step reasoning (needs `GROQ_API_KEY`):

```bash
python chain_of_thought.py
```

➡ Next: [05-anatomy-of-a-prompt](../05-anatomy-of-a-prompt/)
