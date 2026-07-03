# Day 09 — Exercises

```bash
pip install groq python-dotenv   # + GROQ_API_KEY in .env
```

Try each yourself, then check `*_solution.py`.

---

## Exercise 1 — Command-line chatbot 💬
Build a chatbot you can talk to in a loop, that **remembers the conversation**.

**Your task:** in `chatbot.py`, keep a `messages` list (start with a `system` turn). Each loop: read
`input()`, append it as a `user` turn, call `client.chat.completions.create(...)`, print the reply,
**and append the reply as an `assistant` turn**. Quit when the user types `quit`.

*Hint:* the API has no memory — the growing `messages` list *is* the memory. You resend the whole
conversation each call, and remembering the bot's own replies is what keeps it coherent.

➡ Solution: [`chatbot_solution.py`](chatbot_solution.py)

---

## Exercise 2 — Temperature explorer 🌡️
See how temperature changes answers for the **same** prompt.

**Your task:** in `temperature_explorer.py`, pick one prompt and call the model at temperatures
`0.0`, `0.7`, and `1.4`, printing each answer under its temperature. Notice how variety increases.

*Hint:* pass `temperature=t` directly to `client.chat.completions.create(...)`.

➡ Solution: [`temperature_explorer_solution.py`](temperature_explorer_solution.py)
