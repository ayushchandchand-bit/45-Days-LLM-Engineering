"""
Day 18 - Step 3: Retrieve the nearest notes from Chroma.
"""

# `Path` is used to find the shared database folder.
from pathlib import Path

# Chroma stores and searches our saved note vectors.
import chromadb
# SentenceTransformer embeds the user's query before we search.
from sentence_transformers import SentenceTransformer


# `BASE_DIR` points to the Day 18 folder.
BASE_DIR = Path(__file__).resolve().parent.parent
# `DB_DIR` points to the same persistent database folder created in step 1.
DB_DIR = BASE_DIR / "chroma_store"
# `COLLECTION_NAME` is the saved note collection we want to query.
COLLECTION_NAME = "student_notes"

# These are sample natural-language questions we will test against the notes.
QUERIES = [
    "How do I make a prompt more specific?",
    "What does binary search require first?",
    "How do recursive functions stop?",
]


def print_matches(collection, model, query: str, k: int = 2) -> None:
    # Convert the query text into one embedding vector.
    query_embedding = model.encode(query).tolist()
    # Ask Chroma for the top `k` nearest documents to that query vector.
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        # We ask Chroma to return the matched documents, metadata, and distances.
        include=["documents", "metadatas", "distances"],
    )

    # Print the query before its ranked matches.
    print(f"\nQuery: {query}")
    # Walk through the returned parallel lists one rank at a time.
    for rank, (document, metadata, distance) in enumerate(
        zip(
            result["documents"][0],
            result["metadatas"][0],
            result["distances"][0],
        ),
        start=1,
    ):
        # Convert cosine distance into an easy-to-read similarity-like score.
        similarity = 1 - distance
        print(
            f"{rank}. similarity={similarity:.3f} topic={metadata.get('topic', 'unknown')} "
            f"-> {document}"
        )


def main() -> None:
    # Re-open the saved database.
    client = chromadb.PersistentClient(path=str(DB_DIR))
    # Re-open the collection containing the stored notes.
    collection = client.get_collection(COLLECTION_NAME)
    # Load the same embedding model so query vectors live in the same vector space as the notes.
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Print a heading for the retrieval demo.
    print("=" * 72)
    print("Nearest-note retrieval with Chroma")
    print("=" * 72)

    # Run several sample queries so students can see retrieval behavior.
    for query in QUERIES:
        print_matches(collection, model, query)


# Run this module only when the file is executed directly.
if __name__ == "__main__":
    main()
