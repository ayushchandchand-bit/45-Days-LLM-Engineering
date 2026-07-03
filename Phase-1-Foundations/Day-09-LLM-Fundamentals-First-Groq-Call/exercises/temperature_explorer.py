"""
Exercise 2 -- temperature explorer.

Setup: pip install groq python-dotenv  (+ GROQ_API_KEY in .env)
Run:   python temperature_explorer.py
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

prompt = "Write a one-line tagline for a chai startup."

# TODO 1: for each temperature in (0.0, 0.7, 1.4):
#           - call client.chat.completions.create(
#                 model="llama-3.1-8b-instant",
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=t,
#             )
#           - print the temperature and response.choices[0].message.content
