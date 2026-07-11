# Day 21 · Exercises

Build two small LangChain programs yourself. Each has a stub with `# TODO`s and a worked
`_solution.py`. Both run **without a key** (they print the wiring and skip the live call), so you
can check your structure first, then add `GROQ_API_KEY` to `.env` to see the real output.

## 1. Translator Chain (`translator_chain.py`)

Build a reusable **LCEL chain** that translates text into any language.

- A `ChatPromptTemplate` with two variables: `{language}` and `{text}`.
- Compose `prompt | model | StrOutputParser()`.
- Translate the same sentence into three languages with **one `.batch(...)`** call.

> **Skills:** prompt templates (02), LCEL `|` chains (03), `StrOutputParser` + `batch` (03).

## 2. Structured Extractor (`structured_extractor.py`)

Pull **structured data** out of messy text.

- Define a Pydantic `Contact` model: `name`, `email`, `phone`, `company`.
- Use `model.with_structured_output(Contact)` to extract a `Contact` from a signature blob.
- Print the typed fields.

> **Skills:** Pydantic schema + `with_structured_output` (04).

## Run

```bash
python translator_chain_solution.py
python structured_extractor_solution.py
```
(Swap `_solution` for the stub name once you've filled in the TODOs.)

## Stretch

Add a `MessagesPlaceholder("history")` to the translator so it remembers a "translate like a pirate"
style instruction across turns (module 06). Or give the extractor a `list[Contact]` field to pull
**several** contacts from one block of text.

➡ Back to the day: [README](../README.md)
