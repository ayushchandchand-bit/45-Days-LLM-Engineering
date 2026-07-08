# Day 19 — Streamlit From Scratch (turn your Python into a web app)

For 18 days everything you built ran in the **terminal**. Users had to install Python, open a
console, and type. Today that changes. **Streamlit** lets you turn a plain Python script into a
real **web app** — a page with buttons, sliders, text boxes, and a chat window — **without writing
any HTML, CSS, or JavaScript.**

You write Python. Streamlit draws the web page.

```text
your_script.py   --->   streamlit run your_script.py   --->   a website in the browser
```

This is the tool every mini-project in this course is deployed with (Project 1 — the AI
Summarizer — is a Streamlit app), so today is the foundation for everything visible you ship.

---

## The one idea you must understand today

Streamlit has **one weird rule** that confuses everybody on day one. Learn it now and the rest is easy:

> **Every time the user interacts with your app (clicks a button, moves a slider, types), Streamlit
> re-runs your ENTIRE script from the top to the bottom.**

It does **not** run just one function. It runs the whole file again, top to bottom, and redraws the
page from what the code produced this time. Normal variables are wiped and recreated every run.

We spend a whole module (05) on this. Keep it in the back of your mind from module 01: *"the script
re-runs on every click."*

---

## Learning objectives
By the end of today you can:
- Install Streamlit and run any script as a web app with `streamlit run`
- Put text, tables, numbers, JSON, and code blocks on a page with one-line commands
- Collect input with widgets (buttons, text boxes, sliders, dropdowns) and use the values
- Lay a page out with a sidebar, columns, tabs, and expanders
- Explain the **rerun model** and use **`st.session_state`** to remember things between reruns
- Use **caching** so a slow model or API call doesn't repeat on every rerun
- Build a working **AI chat web app** powered by Groq — the terminal chatbot from Day 16, now in a browser

## Modules (work through them in order)

| # | Module | What it teaches | The "aha" |
|--:|--------|-----------------|-----------|
| 01 | [hello-streamlit](01-hello-streamlit/) | Install, `streamlit run`, first page | Python becomes a website with one command |
| 02 | [text-and-data](02-text-and-data/) | `write`, markdown, tables, metrics, JSON | One line puts almost anything on screen |
| 03 | [widgets-and-interaction](03-widgets-and-interaction/) | Buttons, text, sliders, dropdowns | A widget is just a variable you can see |
| 04 | [layout-and-sidebar](04-layout-and-sidebar/) | Sidebar, columns, tabs, expanders | You arrange the page, not just stack it |
| 05 | [session-state-and-rerun](05-session-state-and-rerun/) | The rerun model + `st.session_state` | Why your counter "resets" — and how to fix it |
| 06 | [caching](06-caching/) | `@st.cache_data` / `@st.cache_resource` | Don't reload the model on every click |
| 07 | [groq-chat-app](07-groq-chat-app/) | `st.chat_input`, `st.chat_message`, streaming | Your Day 16 chatbot, now a web app |

Then practise in **[exercises/](exercises/)**.

## Stack for today
- Web UI: `streamlit`
- Tables: `pandas` (installed automatically with Streamlit)
- Chat model (module 07 + one exercise): `groq`

## Setup
```bash
pip install -r requirements.txt
```

Only module 07 and the summarizer exercise need a key. Create a `.env` for those:

```bash
GROQ_API_KEY=your_key_here
```

## How to run — READ THIS, it is different from every other day

You do **NOT** run these files with `python file.py`. Streamlit files are started with the
`streamlit run` command:

```bash
streamlit run 01-hello-streamlit/hello_app.py
```

Your browser opens automatically at **http://localhost:8501**. If it doesn't, copy that URL from the
terminal into your browser. To stop the app, go back to the terminal and press **Ctrl + C**.

> If you accidentally run `python 01-hello-streamlit/hello_app.py`, Streamlit prints a warning like
> *"missing ScriptRunContext"* and nothing useful happens. That is the #1 beginner mistake. Always
> use `streamlit run ...`.

Run each module the same way:
```bash
streamlit run 02-text-and-data/display_app.py
streamlit run 03-widgets-and-interaction/widgets_app.py
streamlit run 04-layout-and-sidebar/layout_app.py
streamlit run 05-session-state-and-rerun/state_app.py
streamlit run 06-caching/caching_app.py
streamlit run 07-groq-chat-app/chat_app.py
```

## Today's exercise
Build two web apps:
- a **BMI calculator** — pure widgets, no AI (recaps the Day 1 exercise as a real web app)
- an **AI text summarizer** — paste text, click a button, Groq returns a TL;DR (a mini version of Project 1)

See [`exercises/`](exercises/).

## For the trainer
A full minute-by-minute delivery script — what to say, what to demo live, and the mistakes students
will make — is in **[DELIVERY-GUIDE.md](DELIVERY-GUIDE.md)**. Read it before class.

> Day 18 gave you retrieval (RAG's "R"). Day 19 gives you a face to put it behind. From here your
> AI is no longer a terminal toy — it is something you can send a friend a link to.

➡ Next (Day 20): wiring a real model behind a Streamlit UI end-to-end, then deploying it free.
