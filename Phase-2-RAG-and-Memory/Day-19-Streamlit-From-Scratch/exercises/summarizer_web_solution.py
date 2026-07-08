"""
Exercise 2 - AI Text Summarizer (web edition).   [SOLUTION]

A mini version of Project 1: paste text, get a structured summary from Groq.

Setup - create a .env with:
    GROQ_API_KEY=your_key_here

Run it:
    streamlit run summarizer_web_solution.py
"""

import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load the API key from .env into the environment.
load_dotenv()


# One shared Groq client for the whole app (module 06). Returns None if no key.
@st.cache_resource
def get_client():
    if not os.getenv("GROQ_API_KEY"):
        return None
    return Groq()


client = get_client()

st.title("AI Text Summarizer")
st.caption("Paste any long text and get a short summary powered by Groq.")

# If there is no key, explain and stop before showing the rest of the UI.
if client is None:
    st.error(
        "No GROQ_API_KEY found. Create a .env file with GROQ_API_KEY=your_key_here, "
        "then restart the app."
    )
    st.stop()

# Sidebar control for how long the summary should be - fed into the prompt.
length = st.sidebar.select_slider(
    "Summary length",
    options=["short", "medium", "long"],
    value="short",
)

# The big box the user pastes text into.
text = st.text_area("Paste text to summarize", height=250)

# The trigger. `st.button` is True only on the rerun right after the click.
if st.button("Summarize"):
    # Guard against an empty box so we never send a blank request.
    if not text.strip():
        st.warning("Please paste some text first.")
    else:
        # st.spinner shows an animated "working..." message while the block runs.
        with st.spinner("Summarizing..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You summarize text for busy students. Reply in Markdown with a "
                            f"one-line **TL;DR** and then 3 key bullet points. Keep it {length}."
                        ),
                    },
                    {"role": "user", "content": text},
                ],
                temperature=0.3,
            )
            # Pull the summary text out of the response.
            summary = response.choices[0].message.content or ""

        # Show the result. Markdown renders the bold TL;DR and the bullets.
        st.subheader("Summary")
        st.markdown(summary)
