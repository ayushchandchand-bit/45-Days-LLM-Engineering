"""
Day 18 - Exercise 2 (STUB): Notes chat assistant with Chroma + Groq.
"""

# `Path` helps us locate the exercise database folder.
from pathlib import Path

# Chroma stores the note vectors and retrieves the best matches.
import chromadb
# `load_dotenv` loads the Groq API key from `.env`.
from dotenv import load_dotenv
# `Groq` is the chat client students will call after retrieval.
from groq import Groq
# SentenceTransformer embeds notes and user questions.
from sentence_transformers import SentenceTransformer


# `BASE_DIR` points to the Day 18 folder.
BASE_DIR = Path(__file__).resolve().parent.parent
# `DB_DIR` is the local Chroma folder for this exercise.
DB_DIR = BASE_DIR / "exercise_notes_chroma"
# `COLLECTION_NAME` is the collection name for the study notes.
COLLECTION_NAME = "study_notes"

# These are the notes the student assistant should search over.
NOTES = [
    "Linked lists are good for cheap inserts but slow random access.",
    "A stack follows last in, first out. Function calls use the call stack.",
    "Prompt examples reduce ambiguity and help the model copy the output format.",
    "Recursion should reduce the problem size and must have a base case.",
]


def main() -> None:
    # Load environment variables so Groq can find the API key.
    load_dotenv()
    # Load the local embedding model.
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # Open the exercise database.
    client = chromadb.PersistentClient(path=str(DB_DIR))
    # Create or reuse the note collection.
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        # Use cosine distance for semantic retrieval.
        metadata={"hnsw:space": "cosine"},
    )

    # TODO: embed NOTES and upsert them into the collection

    # This is the user question we want the assistant to answer.
    question = "Why do recursive functions not run forever?"

    # TODO: retrieve the top 2 notes for the question
    matches = None

    # TODO: add a similarity cutoff. If weak, print a fallback message and return.

    # TODO: create a Groq client, build a context block from the retrieved notes,
    # and ask the model to answer from those notes only.
    llm = Groq()
    # `_` shows that the variable exists for the future TODO but is not used yet.
    _ = llm

    # Print the question so students know what the final answer should address.
    print("Question:", question)
    print("TODO: print the grounded answer")


# Run the exercise only when executed directly.
if __name__ == "__main__":
    main()
