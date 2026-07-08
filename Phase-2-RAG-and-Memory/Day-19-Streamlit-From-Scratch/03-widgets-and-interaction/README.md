# 03 — Widgets and Interaction

A widget is any control the user can touch: a button, a text box, a slider, a dropdown. In
Streamlit, a widget is astonishingly simple to think about:

> **A widget is a function that returns the user's current value.**

```python
name = st.text_input("Your name")   # `name` is whatever the user has typed, as a string
age  = st.slider("Your age", 0, 100, 25)   # `age` is the current slider position, an int
```

That's the whole model. You call the function, you get a value back, you use it like any variable.
No event listeners, no callbacks, no `onclick`. You just read the returned value further down the script.

## The widget menu
| Widget | Returns | Example |
|--------|---------|---------|
| `st.button("Go")` | `bool` — True only on the click's rerun | trigger an action |
| `st.text_input("Name")` | `str` | a single line of text |
| `st.text_area("Notes")` | `str` | a big multi-line box |
| `st.number_input("Qty", 0, 10)` | `int`/`float` | a number with +/- steppers |
| `st.slider("Age", 0, 100, 25)` | `int`/`float` | drag to pick a number |
| `st.selectbox("City", [...])` | the chosen item | a dropdown |
| `st.multiselect("Tags", [...])` | `list` | pick several |
| `st.checkbox("Agree")` | `bool` | on/off |
| `st.radio("Plan", [...])` | the chosen item | pick exactly one, all visible |

## How button clicks *really* work (this trips everyone up)
Remember the rerun rule from module 01. `st.button(...)` returns `True` on **only one rerun**: the
one immediately after the click. On the very next interaction the script reruns and the button is
`False` again. So this pattern:

```python
if st.button("Calculate"):
    st.write("result...")   # shows once, right after the click, then disappears on the next action
```

is perfect for "do this thing now" actions. It is **not** a way to permanently remember that a
button was ever clicked — for that you need `st.session_state` (module 05). Keep this in your back
pocket; it explains a lot of "why did my result vanish?" confusion.

## Other inputs don't need a button
`text_input`, `slider`, etc. already hold their value across reruns (Streamlit remembers widget
values by their label/key). So a live BMI calculator can update the moment a slider moves — no
button required. `demo_widgets.py` shows both styles.

Run it:
```bash
streamlit run widgets_app.py
```

➡ Next: [04-layout-and-sidebar](../04-layout-and-sidebar/) — stop stacking everything in one column.
