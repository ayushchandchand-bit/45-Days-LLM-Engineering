"""
Day 19 - Step 1: Your first Streamlit web app.

Run it (NOT with `python`):
    streamlit run hello_app.py

Then open http://localhost:8501 in your browser (Streamlit usually opens it for you).
Stop the app with Ctrl + C in the terminal.
"""

# `streamlit` is the whole library. By long-standing convention we import it as `st`.
import streamlit as st

# `st.title` draws the biggest heading on the page. This is usually the app's name.
st.title("Hello, Streamlit")

# `st.header` and `st.subheader` are smaller headings for sections.
st.header("I am a web page written in pure Python")
st.subheader("No HTML. No CSS. No JavaScript.")

# `st.write` is the friendly, do-everything function. Give it text and it prints text.
st.write("This whole page is one short Python script.")

# You can pass st.write a normal Python value too - it figures out how to show it.
st.write("Two plus two is:", 2 + 2)

# `st.markdown` accepts Markdown, so you can make **bold**, *italic*, and lists.
st.markdown("Streamlit understands **Markdown**, so you can *style* text easily.")

# --- Meet the rerun rule ---------------------------------------------------
# `st.button` draws a button. It returns True ONLY on the single rerun that
# happens right after the user clicks it, and False every other time.
if st.button("Click me"):
    # This line runs only on the rerun caused by the click.
    st.success("You clicked the button, so Streamlit re-ran the whole script.")

# `st.caption` prints small, greyed-out helper text.
st.caption("Tip: edit this file, press Save, and Streamlit will offer to reload the page.")
