"""
Day 19 - Step 5: The rerun model and st.session_state.

This is THE concept of the day. Keep the terminal visible while you click:
you will see one "SCRIPT RAN" line printed for every single interaction, proving
that Streamlit re-runs the entire file top to bottom each time.

Run it:
    streamlit run state_app.py
"""

import streamlit as st

# This is a PLAIN print to the TERMINAL (not the web page). Because the whole
# script reruns on every interaction, you will see this line appear again and
# again in the terminal as you click around. That is the rerun model, made visible.
print("SCRIPT RAN - Streamlit executed this file from the top.")

st.title("The rerun model")
st.write(
    "Every click reruns this whole script. Watch your terminal: a new "
    "'SCRIPT RAN' line prints each time."
)

st.divider()

# Two counters side by side: one broken, one fixed.
broken_col, working_col = st.columns(2)

# --- The BROKEN counter (plain variable) -------------------------------------
with broken_col:
    st.subheader("Broken counter")
    st.caption("Uses a normal variable. Resets to 0 on every rerun.")

    # `count` is recreated as 0 EVERY time the script runs (which is every click).
    count = 0
    # The button is True only on its click's rerun, so count becomes 1... and only 1.
    if st.button("Add one (broken)"):
        count = count + 1
    # No matter how many times you click, this shows 1, never 2.
    st.write("Count:", count)

# --- The WORKING counter (session_state) -------------------------------------
with working_col:
    st.subheader("Working counter")
    st.caption("Uses st.session_state, which survives reruns.")

    # Initialise ONCE. This guard only runs on the very first script run,
    # because after that the key already exists in session_state.
    if "count" not in st.session_state:
        st.session_state.count = 0

    # Because session_state persists, this genuinely accumulates.
    if st.button("Add one (working)"):
        st.session_state.count += 1

    # Shows 1, 2, 3, 4... as expected.
    st.write("Count:", st.session_state.count)

    # A reset button, to prove we control the stored value.
    if st.button("Reset"):
        st.session_state.count = 0

st.divider()

# Peek at the whole session_state dictionary so students can see what's stored.
st.subheader("What is currently in st.session_state")
st.json(dict(st.session_state))
