"""
Solution -- Exercise 1: few-shot tagger.

Run: python few_shot_tagger_solution.py
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])
MODEL = "llama-3.1-8b-instant"

SYSTEM = "You tag student messages. Reply with only one tag in CAPS."

EXAMPLES = [
    ("I don't understand how recursion works.", "DOUBT"),
    ("Good morning sir!", "GREETING"),
    ("Attached is my week-2 assignment.", "SUBMISSION"),
    ("What time is the canteen open?", "OTHER"),
]


def tag(message):
    messages = [{"role": "system", "content": SYSTEM}]
    for example_in, example_out in EXAMPLES:
        messages.append({"role": "user", "content": example_in})
        messages.append({"role": "assistant", "content": example_out})
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model=MODEL, messages=messages, temperature=0
    )
    return response.choices[0].message.content.strip()


tests = [
    "Sir, here is my assignment for week 3.",     # SUBMISSION
    "Hello everyone, hope you are well.",          # GREETING
    "I'm stuck on the loops question, please help.",  # DOUBT
    "Is the library open on Sunday?",              # OTHER
]

for message in tests:
    print(f"{tag(message):>12}  <-  {message}")
