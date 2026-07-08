"""
Day 19 - Step 3: Widgets - the controls the user interacts with.

The big idea: a widget function RETURNS the user's current value. You just use
that value like a normal variable.

Run it:
    streamlit run widgets_app.py
"""

import streamlit as st

st.title("Widgets: input you can read")

# --- Text inputs -------------------------------------------------------------
st.header("Tell me about yourself")

# `st.text_input` returns whatever the user typed, as a string.
# The second argument is a default value (here, empty).
name = st.text_input("What is your name?", "")

# `st.slider` returns the current slider position. Args: label, min, max, default.
age = st.slider("How old are you?", 0, 100, 20)

# `st.selectbox` returns the option the user picked from a dropdown.
city = st.selectbox("Which city?", ["Delhi", "Mumbai", "Pune", "Chennai", "Other"])

# `st.checkbox` returns True when ticked, False when not.
subscribed = st.checkbox("Send me updates")

# Because widgets just return values, we can use them immediately.
# `name or 'friend'` falls back to 'friend' while the box is still empty.
st.write(f"Hi **{name or 'friend'}**, age {age}, from {city}.")
st.write("Subscribed:", subscribed)

st.divider()

# --- A live calculator (NO button needed) ------------------------------------
st.header("Live tip calculator")
st.caption("Move the widgets and watch the total update instantly - no button.")

# `st.number_input` returns a number. Args include min, max, and a default.
bill = st.number_input("Bill amount (Rs)", min_value=0.0, value=500.0, step=50.0)

# Another slider, this time returning a tip percentage.
tip_percent = st.slider("Tip %", 0, 30, 10)

# Plain Python maths using the widget values.
tip = bill * tip_percent / 100
total = bill + tip

# Show the result. This recomputes on every rerun, i.e. every time a widget moves.
st.metric("Total to pay", f"Rs {total:,.2f}", delta=f"Rs {tip:,.2f} tip")

st.divider()

# --- A button-triggered action -----------------------------------------------
st.header("Button-triggered action")
st.caption("st.button returns True ONLY on the rerun right after you click it.")

# The body of this `if` runs only on the click's rerun, then the message is gone.
if st.button("Give me a cheer"):
    st.success(f"You've got this, {name or 'friend'}! 🎉")
