# 07 — A Groq Chat Web App

Everything comes together here. On Day 16 you built a chatbot that lived in the terminal. Today you
build the **same chatbot as a web app** — a proper chat window in the browser, with message bubbles
and streaming text — and it's barely more code.

## The two chat-specific helpers
Streamlit ships purpose-built chat widgets:

| Call | What it does |
|------|--------------|
| `st.chat_input("Say something")` | the input box pinned to the bottom; returns the user's text when they hit Enter, else `None` |
| `st.chat_message("user")` / `st.chat_message("assistant")` | a chat bubble; use it with `with` and write inside |

```python
with st.chat_message("assistant"):
    st.write("Hello! How can I help?")
```

## The chat pattern (this is just modules 05 + 03 combined)
A chat app is the golden `session_state` pattern plus a loop:

1. **Store the history in `session_state`** — the same `messages` list from Day 16
   (`[{"role": "user", "content": "..."}, ...]`), living in `st.session_state.messages` so it
   survives reruns.
2. **On every rerun, redraw the whole history** — loop over `messages` and render each in a
   `st.chat_message` bubble. (Remember: the script reruns every time, so you repaint the full
   conversation each run. That's normal and cheap.)
3. **When `st.chat_input` returns text:** append the user message, call Groq, append the reply,
   and let the rerun redraw everything.

Because history lives in `session_state`, the bot remembers the conversation — exactly like Day 16,
but now the memory survives Streamlit's reruns instead of a Python `while` loop.

## Streaming (the typewriter effect)
Groq can stream the answer token by token. Streamlit's `st.write_stream(...)` takes that stream and
types it onto the page live, so the user sees words appear instead of waiting for the whole reply.
We use it here; if it ever gives you trouble, the README shows the one-line non-streaming fallback.

## Caching the client
The Groq client is created once with `@st.cache_resource` (module 06) — one shared client for the
whole app, not a new one per rerun.

## Setup
This module needs a key. Create a `.env` in the Day 19 folder (or the repo root):

```bash
GROQ_API_KEY=your_key_here
```

The app checks for the key and shows a friendly error instead of crashing if it's missing.

Run it:
```bash
streamlit run chat_app.py
```

Type in the box at the bottom, press Enter, and watch the reply stream in. Use the sidebar to change
the model, the personality (system prompt), and to clear the chat.

➡ Back to the [Day 19 README](../README.md), then try the [exercises](../exercises/).
