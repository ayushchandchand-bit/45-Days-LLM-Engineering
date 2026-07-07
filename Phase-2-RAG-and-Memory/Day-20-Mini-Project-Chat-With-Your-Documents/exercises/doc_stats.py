"""
Exercise 1 (STUB): Document Stats.

Extract text from a file, chunk it, and print a small report. Fill in the two
functions marked TODO, then run:

    python doc_stats.py

The script writes its own sample_notes.txt, so no setup is needed.
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
    """Return the text inside a .txt, .pdf, or .docx file.

    TODO:
      - if the name ends with .txt  -> data.decode("utf-8")
      - if it ends with .pdf        -> PdfReader(BytesIO(data)), join page.extract_text()
      - if it ends with .docx       -> Document(BytesIO(data)), join paragraph.text
      - otherwise                   -> raise ValueError(...)
    """
    # TODO: implement the dispatch described above.
    raise NotImplementedError


def chunk_words(text: str, size: int = 60, overlap: int = 10) -> list:
    """Split text into overlapping chunks of `size` words.

    TODO:
      - split text into words
      - slide a window of `size` words forward by (size - overlap) each step
      - return the list of joined chunks
    """
    # TODO: implement word chunking.
    raise NotImplementedError


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
