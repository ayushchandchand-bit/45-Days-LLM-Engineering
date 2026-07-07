# 03 · Python Modules & Project Structure

Until now, every script has been **one file**. That's fine for a lesson. But our Day 20 app
does five different jobs — read files, chunk text, embed & store, retrieve, call the LLM. Cram
all of that into one `app.py` and you get a 400-line file nobody can read or test.

The fix is the single most important idea in going from *scripts* to *projects*:

> **A module is just a `.py` file. You can `import` your own files and reuse their functions.**

## Importing your own file

If `text_utils.py` sits next to `main.py`, then `main.py` can use it:

```python
# main.py
import text_utils                       # import the whole module...
text_utils.word_count("hello world")    # ...and call things with the module. prefix

from text_utils import word_count       # ...or import just what you need
word_count("hello world")               # then call it directly
```

Python finds `text_utils` because it's in the same folder. That's the whole trick.

## `if __name__ == "__main__":` — finally explained

You've copied this line all week. Here's what it does:

- When you **run** a file directly (`python main.py`), Python sets that file's `__name__` to
  the string `"__main__"`.
- When you **import** a file, its `__name__` is its module name (e.g. `"text_utils"`).

So `if __name__ == "__main__":` means **"only run this part when I'm the file being run, not
when I'm being imported."** It lets `text_utils.py` offer functions to import *and* have its own
quick self-test that runs only when you execute it directly. Without this guard, importing a
file would run all its top-level code — including any demo prints or, worse, a whole app.

## Why split code into modules?

| One big file                          | Split into modules                                |
|---------------------------------------|---------------------------------------------------|
| Scroll 400 lines to find one function | Open the file named for the job (`file_loader.py`)|
| Everything can touch everything       | Each file has one clear responsibility            |
| Can't test a piece in isolation       | `import chunker` and test just chunking           |
| Merge conflicts when 2 people edit    | People work in different files                    |

Rule of thumb: **one file = one responsibility**, and its filename says what that is.

## A package = a folder of modules

When modules relate, put them in a **folder** — that folder is a *package*. Our project is the
`docchat/` folder: `config.py`, `file_loader.py`, `chunker.py`, `vector_store.py`, `rag.py`,
`llm.py`, `app.py`. Files in the same folder import each other **by name**, exactly like above:

```python
# inside docchat/app.py
from file_loader import load_text
from chunker import chunk_text
```

*(You'll also see two other styles: a leading dot — `from .file_loader import load_text` — used
when a folder is imported as a formal package, and an empty `__init__.py` file that marks a
folder as a package. Our app uses the plain-name style because `streamlit run docchat/app.py`
runs `app.py` as a script and puts its folder on the import path — so siblings are found by
name. Same idea, one less thing to get wrong.)*

## Run it

```bash
python main.py            # runs the app: imports text_utils and uses it
python text_utils.py      # runs text_utils' OWN self-test (thanks to the __name__ guard)
```

Run both and notice: `text_utils.py`'s demo prints appear **only** when you run it directly —
never when `main.py` imports it.

➡ Next: [Build the project → `docchat/`](../docchat/README.md)
