# 03 — Secrets with `.env` and `python-dotenv`

Tomorrow you get a Groq API key. That key is **like a password** — anyone who has it can use your
account (and burn your rate limits). **Rule #1 of AI engineering: never put a key in your code.**

## The pattern everyone uses
1. Put secrets in a file named **`.env`** (key=value pairs):
   ```bash
   # .env  -- never commit this file
   GROQ_API_KEY=gsk_your_real_key
   ```
2. Add `.env` to **`.gitignore`** so Git never tracks it (this repo already does).
3. Load it at runtime with **`python-dotenv`**, then read from `os.environ`:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()                            # reads .env into the environment
   key = os.environ.get("GROQ_API_KEY")     # .get() -> None if missing (no crash)
   ```

## Why `os.environ.get`, not `os.environ[...]`
| Form | If the key is missing |
|------|-----------------------|
| `os.environ["X"]` | raises `KeyError` (crashes) |
| `os.environ.get("X")` | returns `None` — you can check and give a friendly message |

## The golden rules
- **Never** hardcode a key in a `.py` file.
- **Never** commit `.env` (or paste a key in a screenshot / chat).
- If a key ever leaks, **revoke it** and make a new one.

Run the example (it reads a demo variable, no real key needed):

```bash
python dotenv_secrets.py
```

➡ Next: [04-type-hints](../04-type-hints/)
