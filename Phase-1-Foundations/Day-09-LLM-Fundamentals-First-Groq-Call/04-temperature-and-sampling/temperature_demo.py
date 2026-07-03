"""
Temperature in action -- same prompt, low vs high temperature.

Low temperature -> consistent, predictable answers.
High temperature -> varied, creative answers.

Setup: pip install groq python-dotenv  (+ GROQ_API_KEY in .env)
Run:   python temperature_demo.py
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise SystemExit("Set GROQ_API_KEY in a .env file first (see the README).")

client = Groq(api_key=api_key)

prompt = "Suggest a creative name for an AI tutoring app. Reply with just the name."

for temperature in (0.0, 1.2):
    print(f"--- temperature = {temperature} (run twice) ---")
    for _ in range(2):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        print("  ", response.choices[0].message.content.strip())
    print()

print("Low temperature tends to repeat the same answer; high temperature varies.")
