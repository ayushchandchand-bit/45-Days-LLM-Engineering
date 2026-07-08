# 02 — Text and Data

Now that a page exists, let's fill it. Streamlit has a one-line function for almost every kind of
content you'd want to show.

## The display menu
| Call | Shows |
|------|-------|
| `st.write(anything)` | the "magic" function — strings, numbers, dicts, DataFrames, charts... |
| `st.markdown("**md**")` | formatted Markdown |
| `st.title / header / subheader` | headings |
| `st.text("...")` | fixed-width plain text (no Markdown) |
| `st.code("...", language="python")` | a syntax-highlighted code block with a copy button |
| `st.dataframe(df)` | an interactive, scrollable, sortable table |
| `st.table(df)` | a static table (no scrolling) |
| `st.metric("Users", 120, "+8")` | a big KPI number with an up/down delta |
| `st.json({...})` | a collapsible, pretty-printed JSON viewer |
| `st.divider()` | a horizontal line between sections |
| `st.success / info / warning / error` | coloured status boxes |

## `st.write` is the "when in doubt" function
Beginners can lean on `st.write` for almost everything. It inspects whatever you pass and picks a
sensible way to render it: a string becomes text, a dict becomes JSON, a pandas DataFrame becomes a
table, a chart object becomes a chart. As you learn the specific functions (`st.dataframe`,
`st.metric`, ...) you'll reach for those for finer control — but `st.write` is always a safe start.

## Tables come from pandas
Streamlit shows tables using **pandas** DataFrames. Pandas is installed automatically with
Streamlit, so `import pandas as pd` just works. You don't need to know pandas deeply today — a
DataFrame is basically a spreadsheet: named columns and rows. We build a tiny one and hand it to
`st.dataframe`.

## Status boxes tell the user what happened
`st.success`, `st.info`, `st.warning`, and `st.error` draw coloured message boxes. Use them to give
feedback: green for "it worked", red for "something is wrong". You'll use these constantly in real
apps.

Run it:
```bash
streamlit run display_app.py
```

➡ Next: [03-widgets-and-interaction](../03-widgets-and-interaction/) — make the page *do* things.
