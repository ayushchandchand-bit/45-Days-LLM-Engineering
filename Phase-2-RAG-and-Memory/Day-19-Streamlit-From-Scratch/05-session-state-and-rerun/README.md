# 05 — Session State and the Rerun Model

This is the most important module of the day. Spend real time here. Almost every "Streamlit is
weird / my app is broken" moment traces back to this one idea.

## The rerun model, stated plainly
> Every time the user interacts with the app, Streamlit throws away the page and **re-runs your
> entire script from the first line to the last**, then draws the new page from the result.

Not one function. Not "the part near the button." The **whole file, top to bottom, every single
click, keystroke, and slider drag.**

## Why that breaks a normal counter
Here's the intuitive (wrong) way to count button clicks:

```python
count = 0
if st.button("Add one"):
    count = count + 1
st.write(count)   # always prints 1, never 2, 3, 4...
```

Walk through it with the rerun rule:
1. Click the button.
2. Streamlit **reruns the whole script from the top.**
3. Line 1 runs again: `count = 0`. Your previous value is **gone**.
4. The button was clicked, so `count` becomes `0 + 1 = 1`.
5. It prints `1`. Forever.

The variable resets to 0 on every rerun because **line 1 runs every time.** Normal Python variables
cannot survive across reruns. This is the single biggest surprise for beginners.

## The fix: `st.session_state`
`st.session_state` is a dictionary that **Streamlit does NOT wipe between reruns.** It's the app's
memory. Put anything there that must survive: a counter, chat history, a loaded flag.

```python
# Initialise ONCE. This guard means "only set it the very first run".
if "count" not in st.session_state:
    st.session_state.count = 0

# Now it survives reruns, so incrementing actually accumulates.
if st.button("Add one"):
    st.session_state.count += 1

st.write(st.session_state.count)   # 1, 2, 3, 4 ...
```

Two ways to read/write it, both equivalent:
- attribute style: `st.session_state.count`
- dict style: `st.session_state["count"]`

## The golden pattern (memorise this)
```python
if "thing" not in st.session_state:   # 1. initialise once
    st.session_state.thing = <default>

... use and update st.session_state.thing ...   # 2. it persists across reruns
```

You will write this exact three-line guard at the top of nearly every real Streamlit app — including
the chat app in module 07, where `st.session_state.messages` holds the conversation.

## Watch the reruns happen
`state_app.py` prints a line to the **terminal** every time it runs and shows a broken counter next
to a working one, side by side. Click both. Watch the terminal fill with "SCRIPT RAN" lines — proof
that the whole file executes on every click.

Run it:
```bash
streamlit run state_app.py
```

➡ Next: [06-caching](../06-caching/) — if the whole script reruns every click, how do we avoid
reloading a slow model each time?
