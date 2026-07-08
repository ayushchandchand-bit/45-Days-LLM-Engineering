"""
Exercise 2 - AI Text Summarizer (web edition).   [STUDENT STUB]

Paste text, click a button, get a short summary from Groq.

Setup - create a .env with:
    GROQ_API_KEY=your_key_here

Run it:
    streamlit run summarizer_web.py
"""

import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


# TODO 1: cache the Groq client with @st.cache_resource.
#         Return None if os.getenv("GROQ_API_KEY") is missing.
def get_client():
    pass


# TODO 2: title the app with st.title(...)

# TODO 3: if the client is None, st.error(...) a helpful message and st.stop()

# TODO 4: add a st.text_area("Paste text to summarize", height=250)

# TODO 5: add a st.button("Summarize"). When it is clicked AND the text is not
#         empty, call Groq. Wrap the call in `with st.spinner("Summarizing..."):`.
#         Ask for a one-line TL;DR plus 3 key bullet points.
#         Model suggestion: "llama-3.1-8b-instant", temperature 0.3.

# TODO 6: show the returned summary with st.markdown(...)
