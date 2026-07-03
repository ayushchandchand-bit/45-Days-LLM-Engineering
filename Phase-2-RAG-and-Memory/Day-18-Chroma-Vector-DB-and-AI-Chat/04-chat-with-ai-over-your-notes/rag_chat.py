"""
Day 18 - Step 4: Retrieve notes from Chroma, then answer with Groq.
"""

# `Path` helps us locate the saved local database folder.
from pathlib import Path

# Chroma handles storage and nearest-neighbor retrieval.
import chromadb
# `load_dotenv` loads the `GROQ_API_KEY` from a local `.env` file.
from dotenv import load_dotenv
# `Groq` is the hosted chat client we use for the final answer.
from groq import Groq
# SentenceTransformer converts the user's question into an embedding vector.
from sentence_transformers import SentenceTransformer


# `BASE_DIR` points at the Day 18 folder.
BASE_DIR = Path(__file__).resolve().parent.parent
# `DB_DIR` points to the Chroma folder created in earlier steps.
DB_DIR = BASE_DIR / "chroma_store"
# `COLLECTION_NAME` identifies the note collection inside Chroma.
COLLECTION_NAME = "student_notes"
# `MODEL_NAME` is the Groq chat model used to generate the final answer.
MODEL_NAME = "llama-3.3-70b-versatile"


def retrieve_context(collection, embedder, question: str, k: int = 2):
    # Embed the user's question so we can search by meaning instead of keywords.
    query_embedding = embedder.encode(question).tolist()
    # Retrieve the nearest `k` notes from Chroma.
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        # We want the note text, metadata, and distance scores back.
        include=["documents", "metadatas", "distances"],
    )

    # Normalize Chroma's nested response into a simpler list of match dictionaries.
    matches = []
    for document, metadata, distance in zip(
        result["documents"][0],
        result["metadatas"][0],
        result["distances"][0],
    ):
        matches.append(
            {
                # The raw note text that was retrieved.
                "document": document,
                # The note topic stored as metadata.
                "topic": metadata.get("topic", "unknown"),
                # The raw cosine distance returned by Chroma.
                "distance": distance,
                # A friendlier similarity-like score for display.
                "similarity": 1 - distance,
            }
        )
    return matches


def build_context_block(matches) -> str:
    # Build one text block that will be inserted into the LLM prompt.
    lines = []
    for index, match in enumerate(matches, start=1):
        lines.append(
            f"[Source {index} | topic={match['topic']} | similarity={match['similarity']:.3f}] "
            f"{match['document']}"
        )
    # Join each retrieved note with a newline so the prompt stays readable.
    return "\n".join(lines)


def ask_groq(client: Groq, question: str, context_block: str) -> str:
    # Send the retrieved notes and user question to the chat model.
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                # The system message tells the model to stay grounded in the notes.
                "content": (
                    "You answer only from the retrieved notes. If the notes are not enough, say "
                    "'I do not have enough notes to answer that confidently.' Keep answers short."
                ),
            },
            {
                "role": "user",
                # The user message contains both the retrieved context and the question.
                "content": f"Retrieved notes:\n{context_block}\n\nQuestion: {question}",
            },
        ],
        # Low temperature keeps the answer stable and less creative.
        temperature=0.2,
    )
    # Return the text content of the first model choice.
    return response.choices[0].message.content or ""


def main() -> None:
    # Load the Groq API key from `.env`.
    load_dotenv()
    # Create the Groq chat client.
    llm = Groq()
    # Re-open the saved Chroma database.
    chroma_client = chromadb.PersistentClient(path=str(DB_DIR))
    # Re-open the note collection inside that database.
    collection = chroma_client.get_collection(COLLECTION_NAME)
    # Load the local embedding model for query embeddings.
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    # Print a heading so the terminal session is easy to recognize.
    print("=" * 72)
    print("RAG chat over your saved notes")
    print("=" * 72)
    print("Ask a question about the notes. Type 'quit' to exit.")

    # Keep the chat session running until the user quits.
    while True:
        # Read one question from the terminal.
        question = input("\nYou: ").strip()
        # Skip empty input so we do not send blank prompts.
        if not question:
            continue
        # Exit the loop on common quit commands.
        if question.lower() in {"quit", "exit"}:
            print("Bye.")
            break

        # Retrieve the top matching notes for the question.
        matches = retrieve_context(collection, embedder, question, k=2)
        # Convert those matches into a single prompt context block.
        context_block = build_context_block(matches)
        # Ask the chat model to answer using only that retrieved context.
        answer = ask_groq(llm, question, context_block)

        # Show the user exactly which notes were retrieved.
        print("\nRetrieved context:")
        for match in matches:
            print(
                f"- [{match['topic']}] similarity={match['similarity']:.3f} "
                f"{match['document']}"
            )

        # Print the grounded answer from the model.
        print(f"\nAssistant: {answer}")


# Run the chat loop only when this file is executed directly.
if __name__ == "__main__":
    main()
