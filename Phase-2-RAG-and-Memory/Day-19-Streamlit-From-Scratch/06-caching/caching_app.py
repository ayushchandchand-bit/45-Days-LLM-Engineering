"""
Day 19 - Step 6: Caching so slow work does not repeat on every rerun.

Run it:
    streamlit run caching_app.py
"""

import time
import streamlit as st

st.title("Caching: run slow work once, not every rerun")

# --- An UNCACHED slow function -----------------------------------------------
# No decorator, so this genuinely sleeps 2 seconds EVERY time it is called,
# which is every rerun that reaches it.
def slow_uncached(n):
    time.sleep(2)  # pretend this is a slow API call or file read
    return n * n


# --- A CACHED slow function --------------------------------------------------
# `@st.cache_data` stores the result per unique argument. The sleep happens the
# FIRST time for a given `n`; after that the stored answer returns instantly.
@st.cache_data
def slow_cached(n):
    time.sleep(2)  # this only actually runs on a cache MISS
    return n * n


st.header("Uncached: slow every single time")
number1 = st.slider("Pick a number (uncached)", 1, 10, 3)
if st.button("Square it (uncached)"):
    # This waits ~2 seconds on every click, no matter what.
    result = slow_uncached(number1)
    st.success(f"{number1} squared is {result}")

st.divider()

st.header("Cached: slow once per value, then instant")
number2 = st.slider("Pick a number (cached)", 1, 10, 3)
if st.button("Square it (cached)"):
    # First time for a given number: ~2 seconds. Same number again: instant.
    result = slow_cached(number2)
    st.success(f"{number2} squared is {result}")

st.caption(
    "Try clicking 'cached' with the same number twice: the second click is instant. "
    "Then change the number and click again: slow once more (a new cache entry)."
)

st.divider()

# --- The real-world reason we care: loading a model ONCE ---------------------
st.header("The pattern you will actually use")
st.code(
    '''@st.cache_resource            # ONE shared model for the whole app
def get_model():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer("all-MiniLM-L6-v2")

model = get_model()   # loads once; every later rerun reuses the same object''',
    language="python",
)
st.info(
    "Use @st.cache_resource for models, DB connections, and API clients (one shared live object). "
    "Use @st.cache_data for data you compute or fetch (DataFrames, JSON, numbers)."
)
