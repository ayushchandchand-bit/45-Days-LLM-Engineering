"""
Solution -- Exercise 2: temperature explorer.

Run: python temperature_explorer_solution.py
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

prompt = "Write a one-line tagline for a chai startup."

for temperature in (0.0, 0.7, 1.4):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    print(f"temperature {temperature}:")
    print("  ", response.choices[0].message.content.strip())
    print()

print("Higher temperature -> more variety and surprise in the taglines.")
