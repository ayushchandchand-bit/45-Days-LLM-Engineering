"""
Exercise 2 - Structured Extractor (SOLUTION).

Run:
    python structured_extractor_solution.py
"""

from dotenv import load_dotenv
import os

from pydantic import BaseModel, Field
from langchain_groq import ChatGroq

load_dotenv()

MODEL = "llama-3.1-8b-instant"

SIGNATURE = """
Thanks and regards,
Aarav Sharma
Senior Data Analyst, NimbusTech Pvt Ltd
Reach me at aarav.sharma@nimbustech.in or +91 98765 43210
"""


class Contact(BaseModel):
    """Contact details pulled from an email signature."""
    name: str = Field(description="the person's full name")
    email: str = Field(description="their email address")
    phone: str = Field(description="their phone number, including country code if present")
    company: str = Field(description="the company or organisation they work for")


if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY - showing the schema we will ask the model to fill:")
    print("  Contact fields:", list(Contact.model_fields))
else:
    model = ChatGroq(model=MODEL, temperature=0)

    # Bind the schema -> .invoke now returns a validated Contact object.
    extractor = model.with_structured_output(Contact)
    contact = extractor.invoke(f"Extract the contact details from:\n{SIGNATURE}")

    print("Extracted contact:")
    print("  name   :", contact.name)
    print("  email  :", contact.email)
    print("  phone  :", contact.phone)
    print("  company:", contact.company)
