"""
Exercise 2 -- chain-of-thought solver.

Make the model solve a multi-step word problem by reasoning first, then
returning a clean final answer your code can parse.

Setup: pip install groq python-dotenv  (+ GROQ_API_KEY in .env)
Run:   python cot_solver.py
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])
MODEL = "llama-3.1-8b-instant"

problem = (
    "A library has 5 shelves. Each shelf has 9 books. "
    "A class borrows 12 books and returns 4. How many books are in the library now?"
)
# (5 * 9) - 12 + 4 = 45 - 12 + 4 = 37

# TODO 1: write SYSTEM so the model thinks step by step and ends with
#         'Answer: <number>' on the LAST line.
SYSTEM = ""

# TODO 2: call the model with a system + user message, temperature=0.
# TODO 3: print the full reply, then find the line containing "Answer:"
#         and print just that.
