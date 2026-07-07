"""
Day 20 - Step 3: A file that IMPORTS our own module (text_utils.py).

This shows the whole point of modules: text_utils.py holds the reusable logic,
and this file imports and uses it. Run:

    python main.py
"""

# Import the WHOLE module and call things with the module prefix.
import text_utils

# ...or import JUST the names we want, and call them directly.
from text_utils import clean_whitespace, preview


def main() -> None:
    messy = "  Chroma    stores   vectors   for    retrieval  "

    print("=" * 72)
    print("main.py is using functions imported from text_utils.py")
    print("=" * 72)

    # Called with the module prefix (because we did `import text_utils`).
    print("words (via text_utils.word_count):", text_utils.word_count(messy))

    # Called directly (because we did `from text_utils import ...`).
    print("cleaned (via clean_whitespace)   :", repr(clean_whitespace(messy)))
    print("preview (via preview)            :", preview(clean_whitespace(messy), 20))

    # Notice: text_utils.py's OWN self-test did NOT print. Importing it does not
    # run its `if __name__ == "__main__"` block - that only runs when text_utils
    # is the file you execute directly.


if __name__ == "__main__":
    main()
