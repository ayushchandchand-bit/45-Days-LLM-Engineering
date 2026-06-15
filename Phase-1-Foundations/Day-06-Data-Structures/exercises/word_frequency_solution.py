"""
Exercise 2 — Word Frequency Counter (solution).

Run:
    python word_frequency_solution.py
"""

text = """
Artificial intelligence is changing the world. Intelligence in machines
helps the world solve problems. The world of AI is just beginning and the
world is excited about intelligence.
"""

# 1) normalise: lower-case so "The" and "the" count as one word, then split
words = text.lower().split()

# 2 + 3) count, stripping punctuation off each word (the count pattern)
counts = {}
for word in words:
    word = word.strip(".,!?;:")          # "world." and "world" become the same
    if not word:
        continue
    counts[word] = counts.get(word, 0) + 1   # THE dict idiom: missing -> 0, then +1

# 4) rank by count (descending) and show the top 5
ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

print(f"{len(counts)} distinct words. Top 5:")
for word, count in ranked[:5]:
    bar = "#" * count                    # a tiny text bar chart
    print(f"  {word:<14} {count:>2}  {bar}")
