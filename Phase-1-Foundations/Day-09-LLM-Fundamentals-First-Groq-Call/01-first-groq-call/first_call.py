"""
Your first Groq API call.

Groq runs open models (Llama, etc.) on very fast hardware, with a generous
free tier -- perfect for learning.

Setup:
    pip install groq python-dotenv
    # put GROQ_API_KEY=... in a .env file (get a free key at console.groq.com/keys)
Run:
    python first_call.py
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise SystemExit("Set GROQ_API_KEY in a .env file first (see the README).")

# One client object talks to the API for the whole program.
client = Groq(api_key=api_key)

# llama-3.1-8b-instant: fast and free. (Model names change -- see the README.)
# 'messages' is a list of turns; each turn has a role ("user"/"assistant"/"system").
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Explain what an API is in one simple sentence."}
    ],
)

print("Model's answer:")
print(response.choices[0].message.content)

# The response also carries token usage -- handy for cost/limits later.
usage = response.usage
print()
print("Prompt tokens    :", usage.prompt_tokens)
print("Response tokens  :", usage.completion_tokens)
print("Total tokens     :", usage.total_tokens)
