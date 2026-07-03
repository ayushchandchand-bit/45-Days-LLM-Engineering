"""
Counting tokens with Groq.

Tokens drive cost, context limits, and speed -- so it helps to see how text
maps to token counts.

Groq doesn't have a "count only" endpoint, but EVERY response reports how many
tokens the request used (response.usage.prompt_tokens). So we send each sample
with max_tokens=1 (ask for the tiniest possible reply) just to read that count.

Heads-up: prompt_tokens counts the whole formatted request -- your text PLUS a
few tokens of chat scaffolding (role markers). So tiny strings look "too big" by
a fixed handful of tokens. Watch how the count GROWS with longer / rarer / non-
English text rather than reading each number literally.

Setup: pip install groq python-dotenv  (+ GROQ_API_KEY in .env)
Run:   python count_tokens.py
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise SystemExit("Set GROQ_API_KEY in a .env file first (see the README).")

client = Groq(api_key=api_key)

samples = [
    "Hello",
    "I love learning about AI.",
    "Antidisestablishmentarianism",          # one long word -> several tokens
    "namaste, kaise ho aap?",                # Hindi-in-Latin often costs more
]


def prompt_tokens(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": text}],
        max_tokens=1,            # we only want the token count, not a real answer
    )
    return response.usage.prompt_tokens


print("text -> prompt token count")
for text in samples:
    print(f"  {prompt_tokens(text):>3}  <- {text!r}")

print()
print("Notice: token count is NOT the same as word count or character count.")
print("Long/rare words and non-English text use more tokens.")
