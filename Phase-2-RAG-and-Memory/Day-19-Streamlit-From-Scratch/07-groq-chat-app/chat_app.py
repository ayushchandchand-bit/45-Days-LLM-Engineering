"""
Day 19 - Step 7: A Groq-powered chat app in the browser.

This is the Day 16 terminal chatbot, rebuilt as a Streamlit web app. The
conversation lives in st.session_state, so the bot remembers what was said even
though Streamlit re-runs this whole script on every message.

Setup - create a .env with your key:
    GROQ_API_KEY=your_key_here

Run it:
    streamlit run chat_app.py
"""

import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load GROQ_API_KEY from a local .env file into the environment.
load_dotenv()

# `st.set_page_config` sets the browser tab title and icon. Call it once, first.
st.set_page_config(page_title="Groq Chat", page_icon="💬")


# --- The Groq client, created once and cached --------------------------------
# @st.cache_resource gives every rerun the SAME client object instead of building
# a new one each time (see module 06). Returns None if no key is configured.
@st.cache_resource
def get_client():
    # Without a key the Groq() constructor would raise; guard so the app can show
    # a friendly message instead of a traceback.
    if not os.getenv("GROQ_API_KEY"):
        return None
    return Groq()


client = get_client()

st.title("💬 Chat with Groq")

# --- Sidebar: settings (module 04) -------------------------------------------
st.sidebar.header("Settings")
model = st.sidebar.selectbox(
    "Model",
    ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"],
)
system_prompt = st.sidebar.text_area(
    "System prompt (the bot's personality)",
    "You are a friendly, concise assistant for Indian students learning to code.",
)
# A button to wipe the conversation and start over.
if st.sidebar.button("Clear chat"):
    st.session_state.messages = []

# If there is no API key, explain how to fix it and stop before the chat UI.
if client is None:
    st.error(
        "No GROQ_API_KEY found. Create a .env file with GROQ_API_KEY=your_key_here, "
        "then restart the app."
    )
    st.stop()  # st.stop() halts the script here - nothing below runs.

# --- Conversation memory: the golden session_state pattern (module 05) -------
# Initialise the message history ONCE. This list is exactly the Day 16 format:
# a list of {"role": ..., "content": ...} dicts.
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Redraw the whole conversation on every rerun ----------------------------
# Because the script reruns each time, we repaint all past messages every run.
for message in st.session_state.messages:
    # Draw each stored message inside a chat bubble matching its role.
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- The input box, pinned to the bottom -------------------------------------
# st.chat_input returns the typed text when the user hits Enter, else None.
user_text = st.chat_input("Type your message and press Enter")

if user_text:
    # 1. Save and show the user's message.
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.write(user_text)

    # 2. Ask Groq for a reply, streaming it into an assistant bubble.
    with st.chat_message("assistant"):
        # We send the system prompt plus the full running history, so the model
        # has the whole conversation as context (this is what "memory" means).
        messages_to_send = [{"role": "system", "content": system_prompt}]
        messages_to_send.extend(st.session_state.messages)

        # stream=True makes Groq send the answer in pieces as it is generated.
        stream = client.chat.completions.create(
            model=model,
            messages=messages_to_send,
            temperature=0.4,
            stream=True,
        )

        # A tiny generator that yields each chunk's text as it arrives.
        def token_generator():
            for chunk in stream:
                # Some chunks have no text (e.g. the final one); skip those.
                piece = chunk.choices[0].delta.content
                if piece:
                    yield piece

        # st.write_stream types the tokens onto the page live and also RETURNS
        # the full assembled text once streaming finishes.
        reply = st.write_stream(token_generator())

    # 3. Save the assistant's reply so it survives the next rerun.
    st.session_state.messages.append({"role": "assistant", "content": reply})
