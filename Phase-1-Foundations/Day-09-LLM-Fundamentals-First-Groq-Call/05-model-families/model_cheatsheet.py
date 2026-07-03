"""
A tiny decision cheat-sheet for picking a model (no API key needed).

Run:
    python model_cheatsheet.py
"""

# (need, recommendation) pairs -- a starting-point heuristic, not a hard rule.
cheatsheet = [
    ("Most everyday tasks (fast + free)", "Groq llama-3.1-8b-instant"),
    ("Hard reasoning / long complex work", "Groq llama-3.3-70b-versatile"),
    ("Offline / private / no rate limits", "Ollama on your laptop"),
    ("A rare/specialised open model", "Hugging Face Inference"),
    ("Huge free context / Google ecosystem", "Gemini (paid beyond free trials)"),
]

print("What you need              ->  Reach for")
print("-" * 58)
for need, pick in cheatsheet:
    print(f"  {need:38} {pick}")

print()
print("Rule of thumb: start with Groq's small Llama; switch only for a concrete")
print("reason (smarts, privacy, context). Day 12 makes switching one line.")
