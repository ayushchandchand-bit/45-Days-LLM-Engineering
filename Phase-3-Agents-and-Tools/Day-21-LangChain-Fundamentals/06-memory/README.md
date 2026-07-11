# 06 · Conversation Memory

On **Day 16** we gave a chatbot memory by keeping a `messages` list and appending every turn by
hand. LangChain's modern building block for that is **`MessagesPlaceholder`** — a slot in your
prompt that holds *all past turns*. You keep a small history list and pass it in each call, so the
model always sees the whole conversation.

## Two pieces

| Piece | Job |
|-------|-----|
| `MessagesPlaceholder("history")` | a **slot** in the prompt where past turns get injected |
| a plain `history` list | **holds** the past `HumanMessage` / `AIMessage` turns (this is the memory) |

## The pattern

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant."),
    MessagesPlaceholder("history"),   # past turns land here
    ("human", "{input}"),             # the new message
])
chain = prompt | model | StrOutputParser()

history = []                          # THE memory
for user_text in conversation:
    answer = chain.invoke({"history": history, "input": user_text})
    history.append(HumanMessage(user_text))   # remember both sides,
    history.append(AIMessage(answer))         # so the next turn sees them
```

Each turn: inject the running `history` into the prompt → get an answer → append **both** the
user's message and the model's reply. That's why turn 2 ("What is my name?") can answer
"Your name is Riya." — turn 1 is sitting in `history`.

## This is Day 16, in LangChain form

| Day 16 (raw) | Day 21 (LangChain) |
|--------------|--------------------|
| `messages` list of dicts | `history` list of message objects |
| `messages.append({...})` | `history.append(HumanMessage(...))` |
| pass whole list to the API | `MessagesPlaceholder` injects it into the prompt |

Same idea — carry the transcript, re-send it — with typed messages and a prompt slot.

## ⚠️ Don't use `RunnableWithMessageHistory`

Older tutorials wrap the chain in `RunnableWithMessageHistory` to manage the list for you. As of
LangChain 1.x it is **deprecated** in favour of LangGraph's built-in persistence. For a simple chat,
the manual `history` list above is the clean, supported path — and it's precisely what LangGraph
automates next.

## When to reach for LangGraph instead

Keeping the list yourself is fine for a straight transcript. Once you need **branching, tool-calling
loops, summarised long-term memory, or persistence across restarts**, LangChain 1.x steers you to
**LangGraph** (coming up in Phase 3): it stores and re-injects this history for you, keyed by a
thread id. Simple chat → this. Stateful agent → LangGraph.

## Run it

```bash
python conversation_memory.py
```
The offline demo uses a fake model to prove the history is injected (watch the message count grow);
the live demo uses Groq to actually recall the name.

➡ Next: [Exercises](../exercises/README.md), then back to the day [README](../README.md).
