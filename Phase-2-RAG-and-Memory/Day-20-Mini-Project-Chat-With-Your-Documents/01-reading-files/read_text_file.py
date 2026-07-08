"""
Day 20 - Step 1: Read and write plain text files.

The core skill behind "upload a file and chat with it": getting text out of a
file and into a Python string.

Run it:
    python read_text_file.py

This script creates its own sample file first, then reads it back three ways,
so it needs no setup and leaves one file (sample_notes.txt) next to it.
"""

# `Path` from pathlib builds file paths that work on Windows, macOS and Linux.
# Using __file__ means the script finds its sample file no matter where you run
# it from (the current folder can differ from the script's folder).
from pathlib import Path

# The sample file lives right next to this script.
SAMPLE = Path(__file__).resolve().parent / "sample_notes.txt"


def write_sample() -> None:
    """Create a small text file to read back later."""
    # "w" mode CREATES the file (or ERASES it if it already exists), then writes.
    # The `with` block closes the file for us at the end - always use `with`.
    with open(SAMPLE, "w", encoding="utf-8") as f:
        f.write("Line 1: Chroma stores vectors.\n")
        f.write("Line 2: Embeddings turn text into meaning.\n")
        f.write("Line 3: RAG retrieves, then the LLM answers.\n")


def read_whole_file() -> str:
    """Read the entire file into one string with f.read()."""
    # "r" mode opens for reading. encoding="utf-8" decodes the bytes to text.
    with open(SAMPLE, "r", encoding="utf-8") as f:
        return f.read()


def read_as_lines() -> list:
    """Read the file as a list of lines with f.readlines()."""
    with open(SAMPLE, "r", encoding="utf-8") as f:
        # Each item keeps its trailing "\n"; .rstrip() below removes it for display.
        return f.readlines()


def read_line_by_line() -> None:
    """Loop the file one line at a time - the memory-friendly way for big files."""
    # Iterating the file object streams it: only one line is in memory at a time.
    with open(SAMPLE, "r", encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            print(f"  line {number}: {line.rstrip()}")


def main() -> None:
    # 1. Make the sample file so the reads below have something to open.
    write_sample()

    print("=" * 72)
    print("Reading text files three ways")
    print("=" * 72)
    print(f"Sample file: {SAMPLE.name}\n")

    # 2. Whole file as one string.
    print("[1] f.read() -> one string:")
    whole = read_whole_file()
    print(repr(whole))  # repr() shows the \n characters explicitly.
    print(f"    ({len(whole)} characters total)\n")

    # 3. As a list of lines.
    print("[2] f.readlines() -> list of lines:")
    lines = read_as_lines()
    print(f"    got {len(lines)} lines; first item = {lines[0]!r}\n")

    # 4. Streamed, one line per loop.
    print("[3] for line in f -> one line at a time:")
    read_line_by_line()

    # 5. Bonus: a Streamlit upload arrives as BYTES, not text. Here is that step.
    print("\n[4] bytes -> text (what an upload looks like):")
    raw_bytes = SAMPLE.read_bytes()          # exactly what an upload hands you.
    text = raw_bytes.decode("utf-8")         # you decode it yourself.
    print(f"    decoded {len(raw_bytes)} bytes into {len(text)} characters.")


# Run main() only when this file is executed directly (see module 03 for why).
if __name__ == "__main__":
    main()
