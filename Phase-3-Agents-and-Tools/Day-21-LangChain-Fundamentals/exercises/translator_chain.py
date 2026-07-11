"""
Exercise 1 - Translator Chain (STARTER).

Build an LCEL chain that translates text into any language, then translate one
sentence into three languages with a single .batch() call.

Fill in each TODO. Run with:
    python translator_chain.py

It should work with no key (printing the wiring) and, with GROQ_API_KEY set,
print the three real translations.
"""

from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

MODEL = "llama-3.1-8b-instant"
SENTENCE = "Learning never stops."

# TODO 1: Build a ChatPromptTemplate with a system message that says to translate
#         into {language} and reply with ONLY the translation, and a human message
#         that is just {text}.
prompt = ...

# TODO 2: Make a StrOutputParser so the chain returns a plain string.
parser = ...

if not os.getenv("GROQ_API_KEY"):
    # Offline check: prove the prompt fills in correctly.
    print("No GROQ_API_KEY - showing the filled prompt only:")
    # TODO 3: format the prompt for language="Spanish", text=SENTENCE and print each message.
    ...
else:
    model = ChatGroq(model=MODEL, temperature=0)

    # TODO 4: compose the chain: prompt | model | parser
    chain = ...

    # TODO 5: use chain.batch(...) with one dict per language for
    #         "Spanish", "Hindi", "Japanese" (each dict has language + text=SENTENCE).
    languages = ["Spanish", "Hindi", "Japanese"]
    results = ...

    for lang, translation in zip(languages, results):
        print(f"{lang:9}: {translation}")
