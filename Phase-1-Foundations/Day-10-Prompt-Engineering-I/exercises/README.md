# Day 10 — Exercises

```bash
pip install groq python-dotenv   # + GROQ_API_KEY in .env  (same key as Day 9)
```

Try each yourself, then check `*_solution.py`.

---

## Exercise 1 — Few-shot tagger 🏷️
Build a classifier that tags a short student message as one of
**DOUBT**, **SUBMISSION**, **GREETING**, or **OTHER** — using **few-shot** examples.

**Your task:** in `few_shot_tagger.py`, add 3–4 example `(message, tag)` pairs as fake
`user`/`assistant` turns, then send a new message last. Reply with only the tag.

*Hint:* copy the message-building pattern from `03-few-shot/few_shot.py`. Keep `temperature=0`.

➡ Solution: [`few_shot_tagger_solution.py`](few_shot_tagger_solution.py)

---

## Exercise 2 — Chain-of-thought solver 🧮
Make the model solve a multi-step word problem **reliably** and return a clean final answer.

**Your task:** in `cot_solver.py`, write a system prompt that tells the model to **reason step by
step** and end with `Answer: <number>` on the last line. Send a word problem, print the full
reasoning, then parse and print just the final answer.

*Hint:* the system prompt is the whole trick. Parse the line containing `Answer:` (see
`04-chain-of-thought/chain_of_thought.py`).

➡ Solution: [`cot_solver_solution.py`](cot_solver_solution.py)
