"""
Exercise 1 - Translator Chain (SOLUTION).

Run:
    python translator_chain_solution.py
"""

from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

MODEL = "llama-3.1-8b-instant"
SENTENCE = "Learning never stops."

# 1. One reusable template with two blanks.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a translator. Translate the text into {language}. "
               "Reply with ONLY the translation, no notes."),
    ("human", "{text}"),
])

# 2. Parser -> plain string out of the AIMessage.
parser = StrOutputParser()

if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY - showing the filled prompt only:")
    for m in prompt.format_messages(language="Spanish", text=SENTENCE):
        print(f"  [{m.type:>6}] {m.content}")
else:
    model = ChatGroq(model=MODEL, temperature=0)

    # 4. The whole translator in one line.
    chain = prompt | model | parser

    # 5. Translate into three languages at once with batch().
    languages = ["Spanish", "Hindi", "Japanese"]
    inputs = [{"language": lang, "text": SENTENCE} for lang in languages]
    results = chain.batch(inputs)

    print(f'Translating: "{SENTENCE}"\n')
    for lang, translation in zip(languages, results):
        print(f"{lang:9}: {translation}")
