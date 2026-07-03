"""
Day 18 - Exercise 2 (SOLUTION): Notes chat assistant with Chroma + Groq.
"""

# `Path` helps us construct a stable path to the exercise database folder.
from pathlib import Path

# Chroma stores note vectors and performs nearest-neighbor retrieval.
import chromadb
# `load_dotenv` loads the Groq API key from `.env`.
from dotenv import load_dotenv
# `Groq` is the chat client we use after retrieval.
from groq import Groq
# SentenceTransformer embeds notes and the user's question into the same vector space.
from sentence_transformers import SentenceTransformer


# `BASE_DIR` points to the Day 18 folder.
BASE_DIR = Path(__file__).resolve().parent.parent
# `DB_DIR` is the local Chroma folder for this exercise.
DB_DIR = BASE_DIR / "exercise_notes_chroma"
# `COLLECTION_NAME` names the study-note collection.
COLLECTION_NAME = "study_notes"
# `MODEL_NAME` is the Groq chat model used to write the final answer.
MODEL_NAME = "llama-3.3-70b-versatile"

# These notes are the mini knowledge base for the assistant.
NOTES = [
    "Linked lists are good for cheap inserts but slow random access.",
    "A stack follows last in, first out. Function calls use the call stack.",
    "Prompt examples reduce ambiguity and help the model copy the output format.",
    "Recursion should reduce the problem size and must have a base case.",
]


def main() -> None:
    # Load the Groq API key from the local `.env` file.
    load_dotenv()
    # Load the local embedding model.
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # Open the local Chroma database.
    client = chromadb.PersistentClient(path=str(DB_DIR))
    # Create or reuse the study-note collection.
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        # Use cosine distance for retrieval.
        metadata={"hnsw:space": "cosine"},
    )

    # Embed all notes once before storing them.
    note_embeddings = model.encode(NOTES).tolist()
    # Upsert the notes and their vectors into Chroma.
    collection.upsert(
        # Generate simple ids like note-1, note-2, and so on.
        ids=[f"note-{index}" for index in range(1, len(NOTES) + 1)],
        # Store the raw note text as the document field.
        documents=NOTES,
        # Save the embedding vectors beside those notes.
        embeddings=note_embeddings,
    )

    # This is the user question we want to answer with retrieved notes.
    question = "Why do recursive functions not run forever?"
    # Embed the question and retrieve the top 2 nearest notes.
    result = collection.query(
        query_embeddings=[model.encode(question).tolist()],
        n_results=2,
        include=["documents", "distances"],
    )

    # Convert Chroma's nested response into a simpler list of matches.
    matches = []
    for document, distance in zip(result["documents"][0], result["distances"][0]):
        # Convert distance into a similarity-like score for easier reading.
        matches.append({"document": document, "similarity": 1 - distance})

    # Read the best match score so we can decide whether retrieval is trustworthy.
    best_similarity = matches[0]["similarity"]
    # If the best match is too weak, refuse to answer instead of guessing.
    if best_similarity < 0.35:
        print("I do not have enough notes to answer that confidently.")
        return

    # Build the retrieved-note block that will go into the LLM prompt.
    context_block = "\n".join(
        f"- similarity={match['similarity']:.3f} {match['document']}" for match in matches
    )

    # Create the Groq chat client.
    llm = Groq()
    # Ask the chat model to answer only from the retrieved notes.
    response = llm.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                # The system prompt forces the answer to stay grounded in the notes.
                "content": (
                    "Answer only from the provided notes. If the notes are insufficient, say so."
                ),
            },
            {
                "role": "user",
                # The user message contains the retrieved notes plus the question.
                "content": f"Notes:\n{context_block}\n\nQuestion: {question}",
            },
        ],
        # Keep randomness low for more stable grounded answers.
        temperature=0.2,
    )

    # Read the text answer from the first response choice.
    answer = response.choices[0].message.content or ""

    # Print the question for context.
    print("Question:", question)
    # Show the retrieved notes so students can inspect what grounded the answer.
    print("\nRetrieved notes:")
    for match in matches:
        print(f"- similarity={match['similarity']:.3f} {match['document']}")
    # Print the final grounded answer.
    print("\nAnswer:", answer)


# Run the solution only when this file is executed directly.
if __name__ == "__main__":
    main()
