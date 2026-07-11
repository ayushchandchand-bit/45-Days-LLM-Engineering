# 04 · Output Parsers — Text → Data

A model returns **text**. But your program usually wants **data**: a number you can compare,
a list you can loop, fields you can save to a database. Parsers do that last "text → data" step.

## Two levels

| You want… | Use | Returns |
|-----------|-----|---------|
| Clean prose to show a human | `StrOutputParser()` (module 03) | `str` |
| A typed object your code uses | `model.with_structured_output(Model)` | a validated Pydantic object |

## `with_structured_output` — the modern, reliable way

Describe the shape you want with a Pydantic model, then bind it to the model:

```python
from pydantic import BaseModel, Field

class MovieReview(BaseModel):
    title: str = Field(description="the movie's title")
    sentiment: str = Field(description="one of: positive, negative, mixed")
    rating: int = Field(description="a score from 1 to 10")
    reasons: list[str] = Field(description="short bullet reasons")

structured = ChatGroq(model="llama-3.1-8b-instant", temperature=0).with_structured_output(MovieReview)
result = structured.invoke("Extract a review from: I loved Interstellar, 9/10 ...")

result.rating      # -> 9   (a real int, not the string "9")
result.reasons     # -> ["great visuals", "amazing score"]
```

- Each `Field(description=...)` is a **hint** the model reads to fill that field correctly.
- You get back a real `MovieReview` **instance** — validated, typed, no manual `json.loads`.
- If the model returns the wrong shape, Pydantic validation catches it instead of your code
  crashing three steps later.

This is the same **Pydantic** from Day 8 — there it validated *incoming* data; here it defines
the *shape of the model's output*.

## The older way (still useful to recognise)

`JsonOutputParser` / `PydanticOutputParser` add "return JSON in this format" instructions to your
prompt, then parse the reply:
```python
JsonOutputParser().invoke('{"rating": 9}')   # -> {"rating": 9}  (a dict)
```
`with_structured_output` is preferred because it uses the model's native tool/JSON mode and is far
more reliable than begging for JSON in the prompt. Reach for `JsonOutputParser` only with models
that don't support structured output.

## Rule of thumb

> If the next step is **"show text"** → `StrOutputParser`.
> If the next step is **"do something with the data"** → `with_structured_output`.

## Run it

```bash
python structured_output.py
```
The JSON-parsing demo runs with no key; the live extraction into a `MovieReview` needs a key.

➡ Next: [05 · Runnables & Composition](../05-runnables/README.md) — branch and combine steps.
