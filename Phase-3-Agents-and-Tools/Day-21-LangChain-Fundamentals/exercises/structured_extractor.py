"""
Exercise 2 - Structured Extractor (STARTER).

Pull structured contact details out of a messy email signature using
with_structured_output. Fill in each TODO.

Run:
    python structured_extractor.py
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


# TODO 1: Define a Pydantic model 'Contact' with four fields, each with a helpful
#         Field(description=...): name (str), email (str), phone (str), company (str).
class Contact(BaseModel):
    ...


if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY - showing the schema we will ask the model to fill:")
    # TODO 2: print the field names of Contact (hint: Contact.model_fields).
    ...
else:
    model = ChatGroq(model=MODEL, temperature=0)

    # TODO 3: bind the Contact schema to the model with with_structured_output.
    extractor = ...

    # TODO 4: invoke the extractor on SIGNATURE to get a Contact object.
    contact = ...

    print("Extracted contact:")
    print("  name   :", contact.name)
    print("  email  :", contact.email)
    print("  phone  :", contact.phone)
    print("  company:", contact.company)
