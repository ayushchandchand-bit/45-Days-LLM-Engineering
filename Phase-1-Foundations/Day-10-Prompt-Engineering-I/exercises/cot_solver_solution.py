"""
Solution -- Exercise 2: chain-of-thought solver.

Run: python cot_solver_solution.py
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
# (5 * 9) - 12 + 4 = 37

SYSTEM = (
    "You are a careful maths tutor. Solve the problem and show your working "
    "step by step. On the LAST line, write 'Answer: <number>' and nothing else."
)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": problem},
    ],
    temperature=0,
)
reply = response.choices[0].message.content.strip()

print("Full reasoning:")
print(reply)
print()

# Parse just the final answer line so code downstream can use it.
answer_lines = [ln for ln in reply.splitlines() if "answer" in ln.lower()]
print("Parsed ->", answer_lines[-1].strip() if answer_lines else "(not found)")
