"""
06 - Conversation memory the LangChain way (current, non-deprecated).

On Day 16 we gave a chatbot memory by keeping a `messages` list and appending
every turn. LangChain's modern building block for that is MessagesPlaceholder:
a slot in your prompt that holds all past turns. You keep a small history list
and pass it in each call - the model then sees the whole conversation.

(Older tutorials use RunnableWithMessageHistory; it's now DEPRECATED in favour
of LangGraph's persistence. For a simple chat, the pattern below is the clean,
supported approach - and it's exactly what LangGraph automates later.)

The offline demo uses a FAKE model (a plain function) so you can watch history
grow with no key. The live demo uses Groq to really remember your name.

Setup:
    pip install langchain langchain-groq python-dotenv
Run:
    python conversation_memory.py
"""

from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq

load_dotenv()

MODEL = "llama-3.1-8b-instant"

# --- The prompt reserves a slot for past turns ----------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant. Keep answers to one sentence."),
    MessagesPlaceholder("history"),      # <-- all past turns get injected here
    ("human", "{input}"),                # <-- the new user message
])


def run_conversation(model, label):
    """Send two turns through a chain, carrying history ourselves."""
    chain = prompt | model | StrOutputParser()

    history = []   # THE memory: a list of past messages, exactly like Day 16.

    print(f"--- {label} ---")
    for user_text in ["Hi! My name is Riya.", "What is my name?"]:
        # Pass the running history into the prompt's placeholder.
        answer = chain.invoke({"history": history, "input": user_text})

        # Then append BOTH sides of this turn, so the next call remembers it.
        history.append(HumanMessage(user_text))
        history.append(AIMessage(answer))

        print(f"You: {user_text}")
        print(f"Bot: {answer}")
    print(f"(history now holds {len(history)} messages)")
    print()


# --- 1. Offline: a fake model proves history is injected ------------------
def fake_llm(prompt_value):
    """Not a real model - just reports the turns it was handed, to show memory."""
    msgs = prompt_value.to_messages()
    humans = [m.content for m in msgs if m.type == "human"]
    return AIMessage(
        content=f"(I was given {len(msgs)} messages; humans so far: {humans})"
    )

print("OFFLINE demo - watch the message count grow as history is remembered:\n")
run_conversation(RunnableLambda(fake_llm), "offline-fake-model")

# --- 2. Live: a real model actually remembers the name --------------------
if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY set - skipping the live memory demo (this is fine).")
    print("With a key, the Groq model answers turn 2 with 'Your name is Riya.'")
else:
    print("LIVE demo - the model uses the remembered history to answer:\n")
    run_conversation(ChatGroq(model=MODEL, temperature=0), "live-groq")

# --- 3. Note ---------------------------------------------------------------
print("This is Day 16's 'append every turn', now wired through a prompt placeholder.")
print("For heavier state (branching, tools, long-term memory) Phase 3 moves to LangGraph,")
print("which stores and re-injects this history for you automatically.")
