# Day 19 Exercises — build two web apps

Two builds. The first is pure Streamlit (no AI) to lock in widgets and layout. The second wires
Groq behind a button — a mini version of **Project 1 (the AI Content Summarizer)**.

Remember: run these with **`streamlit run`**, not `python`.

---

## Exercise 1 — BMI Calculator (web edition)
File: [`bmi_web.py`](bmi_web.py) · Solution: [`bmi_web_solution.py`](bmi_web_solution.py)

You built a BMI calculator in the terminal on Day 1. Now make it a web app.

**Requirements:**
- A `st.title` for the app.
- A `st.number_input` (or slider) for **weight in kg**.
- A `st.number_input` (or slider) for **height in cm**.
- Compute BMI = `weight / (height_in_metres ** 2)`.
- Show the BMI with `st.metric`, rounded to 1 decimal.
- Show the category with the matching coloured box:
  - `< 18.5` → Underweight (`st.info`)
  - `18.5–24.9` → Normal (`st.success`)
  - `25–29.9` → Overweight (`st.warning`)
  - `>= 30` → Obese (`st.error`)

**Stretch:** put weight and height in two `st.columns` side by side; add a `st.slider` in the sidebar
to switch between metric and (bonus) a different unit.

Run:
```bash
streamlit run bmi_web.py
```

---

## Exercise 2 — AI Text Summarizer (web edition)
File: [`summarizer_web.py`](summarizer_web.py) · Solution: [`summarizer_web_solution.py`](summarizer_web_solution.py)

Paste any long text; get a short summary from Groq. This is the shape of Project 1.

**Requirements:**
- A `st.text_area` for the user to paste text into.
- A `st.button("Summarize")`.
- When clicked (and the text isn't empty), call Groq asking for a short TL;DR + 3 key bullet points.
- Show the summary in the main area (use `st.markdown` or `st.write`).
- While waiting, wrap the API call in `with st.spinner("Summarizing..."):` so the user sees progress.
- Cache the Groq client with `@st.cache_resource`.
- If `GROQ_API_KEY` is missing, show `st.error` instead of crashing.

**Stretch:** add a sidebar `st.slider` for "summary length" (short/medium/long) and feed it into the
prompt; add a "Copy" affordance by showing the result in `st.code`.

Setup — needs a key:
```bash
# .env
GROQ_API_KEY=your_key_here
```

Run:
```bash
streamlit run summarizer_web.py
```

---

> These two apps are the template for every visible thing you ship this course: **widgets in →
> Python/AI in the middle → results out**, all in the browser, all free to deploy.
