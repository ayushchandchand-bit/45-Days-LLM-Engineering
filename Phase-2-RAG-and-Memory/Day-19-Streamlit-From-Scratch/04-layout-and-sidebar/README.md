# 04 — Layout and Sidebar

By default Streamlit stacks everything in one tall column, top to bottom, in the order your code
runs. That's fine for a demo but ugly for a real app. Four tools fix it.

## The four layout tools
| Tool | Use it for |
|------|------------|
| `st.sidebar` | settings/controls in a panel on the left, away from the main content |
| `st.columns(n)` | put things **side by side** |
| `st.tabs([...])` | multiple "pages" the user switches between |
| `st.expander("...")` | hide long/optional content behind a click |

## The sidebar
Anything you want on the left panel, you attach to `st.sidebar`:

```python
model = st.sidebar.selectbox("Model", ["llama-3.1-8b", "llama-3.3-70b"])
temp  = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2)
```

Convention: **settings and knobs go in the sidebar; content goes in the main area.** Every AI app
you build this course puts the model picker and temperature slider in the sidebar. Note that
sidebar widgets return values exactly like normal widgets.

## Columns
`st.columns(3)` returns three column objects. You write into each with a `with` block:

```python
left, middle, right = st.columns(3)
with left:
    st.metric("Users", 120)
with middle:
    st.metric("Signups", 34)
```

You can also pass width ratios: `st.columns([2, 1])` makes the first column twice as wide.

## Tabs and expanders
- `st.tabs(["A", "B"])` gives clickable tabs — great for "Result / Details / Raw JSON".
- `st.expander("Show the prompt")` collapses content until the user clicks — great for hiding the
  long system prompt or debug info so the main screen stays clean.

Both use the same `with` pattern as columns.

Run it:
```bash
streamlit run layout_app.py
```

➡ Next: [05-session-state-and-rerun](../05-session-state-and-rerun/) — the concept everything hinges on.
