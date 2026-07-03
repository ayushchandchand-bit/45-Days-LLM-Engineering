"""
Solution -- Exercise 1: a command-line chatbot with memory.

Run: python chatbot_solution.py   (type 'quit' to exit)
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# The history list IS the memory. We grow it every turn and resend it each call,
# so the model always sees the full conversation so far.
messages = [{"role": "system", "content": "You are a friendly, concise tutor."}]

print("Chatbot ready. Type 'quit' to exit.")
while True:
    user_message = input("You: ")
    if user_message.strip().lower() == "quit":
        print("Bye!")
        break

    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
    )
    reply = response.choices[0].message.content.strip()

    # Remember the bot's own reply so the next turn has full context.
    messages.append({"role": "assistant", "content": reply})
    print("Bot:", reply)
