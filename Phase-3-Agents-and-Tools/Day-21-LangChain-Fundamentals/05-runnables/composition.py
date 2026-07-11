"""
05 - Runnables: branching and combining steps (beyond a straight line).

A chain isn't always a straight pipe. Sometimes you need to:
  * run several steps on the SAME input and collect the results  -> RunnableParallel
  * pass the input through UNCHANGED alongside a computed value   -> RunnablePassthrough
  * drop any plain function into the flow                         -> RunnableLambda

These three are the glue for real pipelines (including RAG). Best part: this
whole file runs OFFLINE - no key needed - because composition is pure Python.

Setup:
    pip install langchain
Run:
    python composition.py
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)

# --- 1. RunnableLambda: any function becomes a chain step ------------------
word_count = RunnableLambda(lambda s: len(s.split()))
print("RunnableLambda word_count.invoke('one two three') =>", word_count.invoke("one two three"))
print()

# --- 2. RunnableParallel: fan the SAME input to many steps ----------------
# A dict of runnables runs each on the input and returns a dict of results.
# (LangChain auto-wraps a plain dict into a RunnableParallel, so you'll often
#  just write the dict directly - shown in step 4.)
analyze = RunnableParallel(
    upper=RunnableLambda(str.upper),
    words=RunnableLambda(lambda s: len(s.split())),
    chars=RunnableLambda(len),
)
print("RunnableParallel runs all branches on one input:")
print(" ", analyze.invoke("langchain is fun"))
print()

# --- 3. RunnablePassthrough: keep the original around ---------------------
# Handy when a later step needs BOTH the raw input and something computed from it.
keep_and_shout = RunnableParallel(
    original=RunnablePassthrough(),          # the input, untouched
    shout=RunnableLambda(str.upper),         # a transformed copy
)
print("RunnablePassthrough keeps the input while you add to it:")
print(" ", keep_and_shout.invoke("hello"))
print()

# --- 4. The pattern you'll reuse forever: the RAG wiring ------------------
# This is EXACTLY how retrieval-augmented generation is wired (Day 20's RAG,
# now in LangChain form). We build the messages here without a model so you can
# SEE the shape; add "| model | parser" and it's a full RAG chain.

def fake_retriever(question: str) -> str:
    """Pretend this searched a vector store and returned the best chunk."""
    return "Refunds are processed within 5-7 business days to the original payment method."

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer ONLY from this context:\n{context}"),
    ("human", "{question}"),
])

# A plain dict is auto-wrapped into a RunnableParallel. Each key is filled by
# its runnable, then the resulting dict feeds the prompt's {context}/{question}.
rag_inputs = {
    "context": RunnableLambda(fake_retriever),   # question -> retrieved text
    "question": RunnablePassthrough(),           # question -> itself, unchanged
}
rag_prompt_chain = rag_inputs | prompt           # add "| model | parser" for the real thing

built = rag_prompt_chain.invoke("How long do refunds take?")
print("The classic RAG wiring, built offline (question -> filled prompt):")
for m in built.to_messages():
    print(f"  [{m.type:>6}] {m.content}")
print()

print("Add '| model | parser' to rag_prompt_chain and you have a full RAG chain.")
print("Same three runnables (Lambda/Parallel/Passthrough) wire up most real pipelines.")
