"""
Day 18 - Step 5: Why Chroma and RAG chat matter.

Offline recap. No model call required.
"""

# Print a separator line so the recap stands out in the terminal.
print("=" * 72)
# Print the title of the recap.
print("DAY 18 RECAP: CHROMA, RETRIEVAL, AND AI CHAT")
# Print another separator line.
print("=" * 72)

# Summarize the concrete tasks built in today's lesson.
print("\n1) What you built")
print("- Embedded notes with a local model")
print("- Stored those vectors inside a persistent Chroma collection")
print("- Re-opened the database from disk")
print("- Retrieved the nearest notes for a new question")
print("- Sent the retrieved notes into an LLM chat prompt")

# Explain the practical benefit of introducing a vector database.
print("\n2) Why the database matters")
print("- Your vectors survive after the script exits")
print("- You can keep adding notes later")
print("- Retrieval becomes a clean database call")
print("- Metadata stays attached to each note")

# Connect the day to the broader RAG idea.
print("\n3) Why this is already RAG")
print("RAG = Retrieval-Augmented Generation")
print("Retrieve relevant notes first, then let the model answer from them.")

# Show the end-to-end pipeline in one line.
print("\n4) The pipeline")
print("notes -> embeddings -> Chroma -> top-k matches -> chat model -> answer")

# Preview the next improvements students will learn later.
print("\n5) What comes next")
print("- Better chunking")
print("- Larger document collections")
print("- Cloud vector storage with pgvector")
print("- Better ranking and citations")

# Place today's lesson in the sequence of Phase 2.
print("\n6) Mental model")
print("Day 16: chat memory")
print("Day 17: embeddings")
print("Day 18: persistent retrieval + AI chat")
print("Day 19: move the same idea to Postgres with pgvector")
