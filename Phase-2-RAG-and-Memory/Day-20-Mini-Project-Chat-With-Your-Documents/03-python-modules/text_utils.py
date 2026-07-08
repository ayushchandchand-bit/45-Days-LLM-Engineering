"""
Day 20 - Step 3: A MODULE - a .py file that offers reusable functions.

This file is meant to be IMPORTED by other files (see main.py). It also has its
own small self-test at the bottom that runs only when you execute this file
directly - that is what the `if __name__ == "__main__"` guard is for.

Try both:
    python text_utils.py    # runs the self-test below
    python main.py          # imports these functions and uses them
"""


def word_count(text: str) -> int:
    """Return how many whitespace-separated words are in `text`."""
    # .split() with no argument splits on any run of whitespace and drops blanks.
    return len(text.split())


def clean_whitespace(text: str) -> str:
    """Collapse runs of whitespace into single spaces and trim the ends."""
    # " ".join(text.split()) is the classic one-liner to normalise spacing.
    return " ".join(text.split())


def preview(text: str, limit: int = 40) -> str:
    """Return the first `limit` characters, with an ellipsis if we cut it."""
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


# --- Self-test: runs ONLY when you do `python text_utils.py` -----------------
# When another file does `import text_utils`, __name__ is "text_utils", so this
# block is skipped and only the functions above are made available.
if __name__ == "__main__":
    print("Self-test of text_utils (only runs when executed directly):")
    sample = "  the   quick brown   fox  "
    print("  word_count      ->", word_count(sample))
    print("  clean_whitespace->", repr(clean_whitespace(sample)))
    print("  preview         ->", preview("a very long sentence " * 5))
