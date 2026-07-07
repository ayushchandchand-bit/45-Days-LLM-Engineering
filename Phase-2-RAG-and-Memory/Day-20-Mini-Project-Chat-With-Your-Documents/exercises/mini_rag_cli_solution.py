"""
Exercise 2 (SOLUTION): Mini RAG in the terminal.

    python mini_rag_cli_solution.py

Runs two demo questions, then drops into a You: loop (type 'quit' to exit).
Retrieval works with no API key; the written answer needs GROQ_API_KEY.
"""

import os

import chromadb
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

DOCUMENT = (
    "Softpro School of AI runs a 46-day AI development summer training. "
    "The course is free-tier first and uses Groq for the language model. "
    "Embeddings are created locally with sentence-transformers. "
    "Chroma is the vector database used to store and retrieve document chunks. "
    "Refunds for the paid cohort are processed within seven working days. "
    "Classes run for three hours a day across four project-based phases."
)


def chunk_words(text, size=25, overlap=5):
    words = text.split()
    step = max(1, size - overlap)
    out = []
    for start in range(0, len(words), step):
        out.append(" ".join(words[start:start + size]))
        if start + size >= len(words):
            break
    return out


def build_index(embedder, chunks):
    client = chromadb.EphemeralClient()
    collection = client.get_or_create_collection(
        "doc", metadata={"hnsw:space": "cosine"}
    )
    embeddings = embedder.encode(chunks).tolist()
    collection.add(
        ids=[f"c{i}" for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings,
    )
    return collection


def retrieve(collection, embedder, question, k=2):
    query_vec = embedder.encode(question).tolist()
    result = collection.query(
        query_embeddings=[query_vec],
        n_results=min(k, collection.count()),
        include=["documents", "distances"],
    )
    return [
        (1 - dist, doc)
        for doc, dist in zip(result["documents"][0], result["distances"][0])
    ]


def answer(question, matches):
    if not os.getenv("GROQ_API_KEY"):
        return None
    from groq import Groq
    context = "\n".join(doc for _, doc in matches)
    client = Groq()
    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Answer only from the context. If it's not there, say so."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
        ],
        temperature=0.2,
    )
    return resp.choices[0].message.content


def ask(collection, embedder, question):
    print(f"\nYou: {question}")
    matches = retrieve(collection, embedder, question, k=2)
    for sim, doc in matches:
        print(f"  [{sim:.2f}] {doc}")
    reply = answer(question, matches)
    print(f"  Bot: {reply}" if reply else "  (set GROQ_API_KEY for a written answer)")


def main() -> None:
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    collection = build_index(embedder, chunk_words(DOCUMENT))

    # Two built-in demo questions so the pipeline is visible even when piped.
    for q in ["How long do refunds take?", "Which vector database is used?"]:
        ask(collection, embedder, q)

    # Then an interactive loop.
    print("\nAsk your own questions (type 'quit' to exit).")
    while True:
        try:
            q = input("\nYou: ").strip()
        except EOFError:
            break
        if not q:
            continue
        if q.lower() in {"quit", "exit"}:
            break
        matches = retrieve(collection, embedder, q, k=2)
        for sim, doc in matches:
            print(f"  [{sim:.2f}] {doc}")
        reply = answer(q, matches)
        print(f"  Bot: {reply}" if reply else "  (set GROQ_API_KEY for a written answer)")


if __name__ == "__main__":
    main()
