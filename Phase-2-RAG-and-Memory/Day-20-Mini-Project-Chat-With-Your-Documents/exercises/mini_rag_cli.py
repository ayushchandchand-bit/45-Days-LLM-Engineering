"""
Exercise 2 (STUB): Mini RAG in the terminal - the app, minus Streamlit.

Chunk a document, embed it into Chroma, retrieve the best chunks per question,
and (if a GROQ_API_KEY is set) answer with Groq. Fill in the TODOs, then run:

    python mini_rag_cli.py

Retrieval works with NO API key - the answer step is the only part that needs one.
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
    """Create an in-memory Chroma collection and add the embedded chunks.

    TODO:
      - client = chromadb.EphemeralClient()
      - collection = client.get_or_create_collection("doc", metadata={"hnsw:space": "cosine"})
      - embeddings = embedder.encode(chunks).tolist()
      - collection.add(ids=[...], documents=chunks, embeddings=embeddings)
      - return collection
    """
    # TODO: implement.
    raise NotImplementedError


def retrieve(collection, embedder, question, k=2):
    """Return a list of (similarity, chunk) for the top-k matches.

    TODO:
      - embed the question
      - collection.query(query_embeddings=[...], n_results=k, include=["documents","distances"])
      - turn distances into similarity = 1 - distance
      - return a list of (similarity, document) tuples
    """
    # TODO: implement.
    raise NotImplementedError


def answer(question, matches):
    """If a GROQ_API_KEY exists, return a grounded answer; else return None."""
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


def main() -> None:
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    collection = build_index(embedder, chunk_words(DOCUMENT))

    for q in ["How long do refunds take?", "Which vector database is used?"]:
        print(f"\nYou: {q}")
        matches = retrieve(collection, embedder, q, k=2)
        for sim, doc in matches:
            print(f"  [{sim:.2f}] {doc}")
        reply = answer(q, matches)
        print(f"  Bot: {reply}" if reply else "  (set GROQ_API_KEY for a written answer)")


if __name__ == "__main__":
    main()
