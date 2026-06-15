"""
Exercise 2 — Word Frequency Counter (STUDENT STUB).

Count how many times each word appears, then show the top 5.

Run:
    python word_frequency.py
"""

text = """
Artificial intelligence is changing the world. Intelligence in machines
helps the world solve problems. The world of AI is just beginning and the
world is excited about intelligence.
"""

# TODO 1: lower-case the text and .split() it into a list of words
# TODO 2: for each word, strip punctuation -> word.strip(".,!?;:")
# TODO 3: build a counts dict using counts[word] = counts.get(word, 0) + 1
# TODO 4: sort counts.items() by the count (descending) and print the top 5
#         hint: sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
