"""
Day 18 - Exercise 1 (SOLUTION): FAQ retrieval bot with Chroma.
"""

# `Path` helps us create a local Chroma folder relative to this file.
from pathlib import Path

# Chroma stores and searches FAQ vectors.
import chromadb
# SentenceTransformer turns questions into embeddings.
from sentence_transformers import SentenceTransformer


# `BASE_DIR` points to the Day 18 folder.
BASE_DIR = Path(__file__).resolve().parent.parent
# `DB_DIR` is the database folder for this exercise.
DB_DIR = BASE_DIR / "exercise_faq_chroma"
# `COLLECTION_NAME` names the FAQ collection inside Chroma.
COLLECTION_NAME = "faq_collection"

# These FAQ items are the knowledge base we want to search.
FAQS = [
    {
        "id": "faq-1",
        "question": "How do I request a refund?",
        "answer": "Refunds can be requested within 7 days from the orders page.",
    },
    {
        "id": "faq-2",
        "question": "When will my certificate be issued?",
        "answer": "Certificates are issued after the final demo and attendance check.",
    },
    {
        "id": "faq-3",
        "question": "How can I reset my portal password?",
        "answer": "Use the forgot-password link on the login page and follow the email steps.",
    },
]


def main() -> None:
    # Load the local embedding model.
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # Open the local Chroma database.
    client = chromadb.PersistentClient(path=str(DB_DIR))
    # Create or reuse the FAQ collection.
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        # Use cosine distance for nearest-neighbor search.
        metadata={"hnsw:space": "cosine"},
    )

    # Embed every FAQ question once so we can store them in Chroma.
    question_embeddings = model.encode([faq["question"] for faq in FAQS]).tolist()

    # Store the FAQ questions, answers, and vectors together in the collection.
    collection.upsert(
        # Each FAQ gets a stable id.
        ids=[faq["id"] for faq in FAQS],
        # The stored document text is the FAQ question.
        documents=[faq["question"] for faq in FAQS],
        # The answer is stored in metadata so we can retrieve it later.
        metadatas=[{"answer": faq["answer"]} for faq in FAQS],
        # These are the question embeddings used for semantic search.
        embeddings=question_embeddings,
    )

    # Simulate a user asking the same thing in different words.
    user_question = "How do I get my payment back?"
    # Embed the user's question and retrieve the closest FAQ.
    result = collection.query(
        query_embeddings=[model.encode(user_question).tolist()],
        n_results=1,
        include=["documents", "metadatas", "distances"],
    )

    # Pull the matched FAQ question out of the response.
    matched_question = result["documents"][0][0]
    # Pull the stored answer out of metadata.
    answer = result["metadatas"][0][0]["answer"]
    # Convert distance to a similarity-like value for display.
    similarity = 1 - result["distances"][0][0]

    # Print the question, the matched FAQ, and the final answer.
    print("User question:", user_question)
    print("Matched FAQ :", matched_question)
    print("Similarity  :", f"{similarity:.3f}")
    print("Answer      :", answer)


# Run the solution only when executed directly.
if __name__ == "__main__":
    main()
