# 01 — Hello, Streamlit

Your very first web page written in nothing but Python.

## What Streamlit is (say this to the room)
Streamlit is a Python library. You call functions like `st.title(...)` and `st.button(...)`, and
Streamlit turns each call into a piece of a web page. There is **no HTML, no CSS, no JavaScript, no
front-end framework**. If you can write a Python script, you can build a web app.

## The single most important command
Streamlit apps are **not** started with `python`. They are started with `streamlit run`:

```bash
streamlit run hello_app.py
```

That command:
1. starts a tiny web server on your machine,
2. opens your browser at **http://localhost:8501**, and
3. runs your script to draw the page.

Stop it with **Ctrl + C** in the terminal.

> ⚠️ **The #1 beginner mistake:** running `python hello_app.py`. That prints a warning about a
> "missing ScriptRunContext" and shows nothing. Streamlit code only comes alive under `streamlit run`.

## The first three functions
| Call | What appears |
|------|--------------|
| `st.title("...")` | big page heading |
| `st.header("...")` / `st.subheader("...")` | smaller headings |
| `st.write("...")` | the everything function — text, numbers, tables, almost anything |

## The rerun rule — meet it now
At the bottom of `hello_app.py` there is a button. Click it and watch: a message appears. Streamlit
**re-ran the whole file** to redraw the page. This top-to-bottom rerun on every interaction is the
heart of Streamlit — we go deep on it in module 05. For now just notice that it happens.

## Live reload — the nicest part
While the app is running, **edit the file and save it.** Streamlit notices and shows a *"Source file
changed"* prompt in the top-right — click **Rerun** (or set it to "Always rerun"). You never restart
the server while developing. Change code → save → see it. Demo this live; it always gets a reaction.

Run it:
```bash
streamlit run hello_app.py
```

➡ Next: [02-text-and-data](../02-text-and-data/) — all the ways to put content on the page.
