"""
Exercise 1 (SOLUTION): Document Stats.

    python doc_stats_solution.py
"""

from io import BytesIO
from pathlib import Path

from docx import Document
from pypdf import PdfReader

SAMPLE = Path(__file__).resolve().parent / "sample_notes.txt"

SAMPLE_TEXT = (
    "Embeddings turn text into vectors that capture meaning. "
    "Chroma stores those vectors and retrieves the nearest ones. "
    "RAG retrieves the most relevant chunks, then the LLM answers using them. "
    "Chunking splits a long document into small overlapping passages so retrieval "
    "stays focused and prompts stay small."
)


def load_text(filename: str, data: bytes) -> str:
    """Return the text inside a .txt, .pdf, or .docx file."""
    name = filename.lower()
    if name.endswith(".txt"):
        return data.decode("utf-8")
    if name.endswith(".pdf"):
        reader = PdfReader(BytesIO(data))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    if name.endswith(".docx"):
        doc = Document(BytesIO(data))
        return "\n".join(p.text for p in doc.paragraphs)
    raise ValueError(f"Unsupported file type: {filename}")


def chunk_words(text: str, size: int = 60, overlap: int = 10) -> list:
    """Split text into overlapping chunks of `size` words."""
    words = text.split()
    if not words:
        return []
    step = max(1, size - overlap)
    chunks = []
    for start in range(0, len(words), step):
        chunks.append(" ".join(words[start:start + size]))
        if start + size >= len(words):
            break
    return chunks


def main() -> None:
    SAMPLE.write_text(SAMPLE_TEXT, encoding="utf-8")
    data = SAMPLE.read_bytes()

    text = load_text(SAMPLE.name, data)
    words = text.split()
    chunks = chunk_words(text)

    print("=" * 60)
    print("Document stats")
    print("=" * 60)
    print(f"File      : {SAMPLE.name}")
    print(f"Characters: {len(text)}")
    print(f"Words     : {len(words)}")
    print(f"Chunks    : {len(chunks)}   (size=60 words, overlap=10)")
    print(f"Longest word: {max(words, key=len)}")


if __name__ == "__main__":
    main()
