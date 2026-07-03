# Day 10 — Prompt Engineering I: System, Zero-Shot, Few-Shot & Chain-of-Thought

Yesterday you made a model talk. Today you make it **do what you actually want**. The same model
gives wildly different answers depending on *how you ask* — that skill is **prompt engineering**, and
it's the cheapest, fastest lever you have (no fine-tuning, no extra cost).

## Learning objectives
By the end of today you can:
- Steer a model's role, rules, and tone with a **system prompt**
- Write clear **zero-shot** instructions (ask well, no examples)
- Teach a task by example with **few-shot** prompting
- Unlock step-by-step reasoning with **chain-of-thought**
- Assemble all four into a reliable prompt using a **checklist**

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [system-prompts](01-system-prompts/) | Set the assistant's role and rules with a `system` message |
| 02 | [zero-shot](02-zero-shot/) | Ask directly with crisp instructions — no examples |
| 03 | [few-shot](03-few-shot/) | Teach the task with a few worked examples |
| 04 | [chain-of-thought](04-chain-of-thought/) | "Think step by step" for multi-step reasoning |
| 05 | [anatomy-of-a-prompt](05-anatomy-of-a-prompt/) | The reusable checklist; put it all together |

Then practise in **[exercises/](exercises/)**.

## Setup
```bash
pip install -r requirements.txt   # groq + python-dotenv (already installed from Day 9)
```
Reuse your **free** Groq key from Day 9 (`GROQ_API_KEY` in a `.env`). New here?
Get one at [console.groq.com/keys](https://console.groq.com/keys).

## How to run
```bash
python 01-system-prompts/system_prompts.py
```
Every script uses Groq's `llama-3.1-8b-instant` and **temperature 0** so the teaching output is
stable run-to-run.

## The one idea to remember
> The model is not a mind reader. **Role + clear task + examples + room to reason** turns a vague
> request into a dependable answer. Each module adds one of those pieces.

➡ Next (Day 11): Prompt engineering II — structured outputs with Pydantic and JSON mode.
