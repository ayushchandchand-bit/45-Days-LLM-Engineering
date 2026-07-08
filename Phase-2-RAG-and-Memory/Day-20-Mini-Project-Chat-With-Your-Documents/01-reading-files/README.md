# 01 · Reading & Writing Files

Every app we've built so far invented its data in Python (a `NOTES = [...]` list). Real apps
read data **from files** — a resume, a textbook, an export. Today's project lets the user
**upload** files, so the very first skill we need is: *open a file and get its text*.

## The one pattern to remember: `with open(...)`

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()
# the file is automatically closed here, even if an error happened inside
```

- `open(path, mode, encoding=...)` returns a **file object**.
- The `with` block **auto-closes** the file when you leave it. Always use `with` — forgetting
  to close files leaks resources and can lock the file on Windows.
- `encoding="utf-8"` tells Python how bytes map to characters. Text files are bytes on disk;
  UTF-8 is the modern default. Leaving it out uses the OS default and breaks on other machines.

## Modes

| Mode  | Meaning                        | If file exists | If missing |
|-------|--------------------------------|----------------|------------|
| `"r"` | read (default)                 | reads it       | **error**  |
| `"w"` | write — **truncates** first    | **erased!**    | creates    |
| `"a"` | append — add to the end        | adds to end    | creates    |
| `"rb"`/`"wb"` | binary (bytes, no text) | —              | —          |

⚠️ `"w"` erases the file the instant you open it. Never open a file you care about in `"w"`
to "peek" at it.

## Reading: three ways

| Call            | Returns                              | Use when                       |
|-----------------|--------------------------------------|--------------------------------|
| `f.read()`      | the whole file as one string         | small files, you want it all   |
| `f.readlines()` | a list of lines (each keeps its `\n`)| you want to number/loop lines  |
| `for line in f` | one line per loop, streamed          | big files (memory-friendly)    |

## Text vs bytes (this matters on Day 20)

A file on disk is always **bytes**. `open(..., "r", encoding=...)` decodes those bytes into a
`str` for you. When a file arrives as raw bytes (like a Streamlit upload), you decode it
yourself:

```python
raw_bytes = uploaded_file.read()        # bytes, e.g. b"Hello"
text = raw_bytes.decode("utf-8")        # str,   "Hello"
```

PDFs and DOCX are **not** plain text — you can't `.decode()` them. They need a library to pull
the words out. That's the next module.

## Run it

```bash
python read_text_file.py
```

The script writes a small sample file, then reads it back three different ways so you can see
the difference.

➡ Next: [02 · Reading PDF & DOCX](../02-reading-pdf-and-docx/README.md)
