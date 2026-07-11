"""
04 - Output parsers: turn a reply into typed DATA, not prose.

A model returns text. But often you want a Python object you can use directly:
a rating you can compare, a list you can loop, fields you can store. Parsers do
that final "text -> data" step.

Two levels:
  * StrOutputParser  -> plain string (module 03).
  * with_structured_output(PydanticModel) -> a validated object with real fields.
    This is the modern, reliable way to get JSON out of a model.

Offline, we show a JSON parser working on a fixed string. The live part uses a
key to make the model actually fill the structure.

Setup:
    pip install langchain langchain-groq python-dotenv
Run:
    python structured_output.py
"""

from dotenv import load_dotenv
import os

from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq

load_dotenv()

MODEL = "llama-3.1-8b-instant"


# --- 1. Describe the shape you want with Pydantic -------------------------
# Each Field's description is a HINT the model reads to fill it correctly.
# (Pydantic is the same tool from Day 8 - here it defines our output schema.)
class MovieReview(BaseModel):
    """A structured summary of a movie review."""
    title: str = Field(description="the movie's title")
    sentiment: str = Field(description="one of: positive, negative, mixed")
    rating: int = Field(description="a score from 1 to 10")
    reasons: list[str] = Field(description="short bullet reasons for the rating")


# --- 2. Offline: a parser turns a JSON string into Python -----------------
# This is what the model *would* return; JsonOutputParser turns text -> dict.
fake_model_output = '{"title": "Inception", "sentiment": "positive", "rating": 9, "reasons": ["clever plot", "great score"]}'
parsed = JsonOutputParser().invoke(fake_model_output)
print("JsonOutputParser turned text into a real dict:")
print("  type:", type(parsed).__name__)
print("  rating + 1:", parsed["rating"] + 1, "  (it's a real int, we can do maths)")
print()

# --- 3. Live: make the model fill the structure for us --------------------
review_text = (
    "I finally watched Interstellar. The visuals and the score blew me away, "
    "though the middle dragged a bit. Still, easily one of the best sci-fi films I've seen."
)

if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY set - skipping the live structured call (this is fine).")
    print("With a key, this is the whole trick:")
    print("    structured = ChatGroq(...).with_structured_output(MovieReview)")
    print("    result = structured.invoke(review_text)   # -> a MovieReview object")
else:
    model = ChatGroq(model=MODEL, temperature=0)

    # with_structured_output binds the schema to the model. Now .invoke returns
    # a MovieReview instance directly -- no manual JSON parsing, and it's validated.
    structured = model.with_structured_output(MovieReview)
    result = structured.invoke(f"Extract a structured review from:\n{review_text}")

    print("Got back a", type(result).__name__, "object with real fields:")
    print("  title    :", result.title)
    print("  sentiment:", result.sentiment)
    print("  rating   :", result.rating, "/ 10")
    print("  reasons  :")
    for r in result.reasons:
        print("     -", r)

# --- 4. Takeaway ----------------------------------------------------------
print()
print("StrOutputParser -> a string for humans.")
print("with_structured_output(Model) -> a typed object for your code. Prefer it")
print("whenever the next step is 'do something with the data', not 'show text'.")
