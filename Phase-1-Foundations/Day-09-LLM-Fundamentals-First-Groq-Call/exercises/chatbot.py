"""
Exercise 1 -- a command-line chatbot that remembers the conversation.

The API has NO memory of its own: each call is independent. To make the bot
"remember", you keep a list of messages and resend the whole list every time.

Setup: pip install groq python-dotenv  (+ GROQ_API_KEY in .env)
Run:   python chatbot.py
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# TODO 1: make a history list, e.g.
#           messages = [{"role": "system", "content": "You are a friendly tutor."}]
# TODO 2: loop forever:
#           - read the user's message with input("You: ")
#           - if it is "quit", break
#           - append {"role": "user", "content": <their text>} to messages
#           - call client.chat.completions.create(model="llama-3.1-8b-instant", messages=messages)
#           - read reply = response.choices[0].message.content
#           - append {"role": "assistant", "content": reply} to messages  (this is the "memory")
#           - print the reply
