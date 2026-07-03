"""
Exercise 1 -- few-shot tagger.

Tag a short student message as one of: DOUBT, SUBMISSION, GREETING, OTHER.
Use FEW-SHOT examples (fake user/assistant turns) to lock the label set.

Setup: pip install groq python-dotenv  (+ GROQ_API_KEY in .env)
Run:   python few_shot_tagger.py
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])
MODEL = "llama-3.1-8b-instant"

SYSTEM = "You tag student messages. Reply with only one tag in CAPS."

# TODO 1: fill EXAMPLES with 3-4 (message, tag) pairs covering the four tags.
EXAMPLES = [
    # ("I don't understand recursion.", "DOUBT"),
    # ...
]

# TODO 2: build a messages list:
#           - start with {"role": "system", "content": SYSTEM}
#           - for each (msg, tag) in EXAMPLES: append a user turn then an assistant turn
#           - append the real message last
# TODO 3: call client.chat.completions.create(model=MODEL, messages=..., temperature=0)
#         and print response.choices[0].message.content

new_message = "Sir, here is my assignment for week 3."
# Expected tag: SUBMISSION
