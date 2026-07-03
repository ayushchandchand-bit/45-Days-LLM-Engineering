"""
Day 17 - Step 1: What is an embedding? (pure Python, NO libraries)

We pretend each word is described by just TWO made-up features:
    axis 1 = "how animal is it?"     axis 2 = "how vehicle is it?"
So every word becomes a point (x, y). Words with similar meaning sit close
together. We measure "close" with plain straight-line (Euclidean) distance.

This is embeddings in miniature: text -> numbers, and nearby = similar.
Real models (module 02) use hundreds of features picked by a trained model
instead of our 2 hand-made ones -- but the idea is exactly this.

Run:   python coordinates.py
"""

from math import sqrt

# Each word -> a 2-D vector (animal-ness, vehicle-ness). Hand-made on purpose.
WORDS = {
    "cat":   (0.9, 0.1),
    "dog":   (0.8, 0.2),
    "car":   (0.1, 0.9),
    "truck": (0.2, 0.8),
}


def distance(a, b):
    """Straight-line distance between two points. Smaller = more alike."""
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def main():
    print("Each word is a point (animal-ness, vehicle-ness):\n")
    for word, vec in WORDS.items():
        print(f"  {word:6} -> {vec}")

    # Compare everything to 'cat' and sort from closest to farthest.
    target = "cat"
    print(f"\nHow close is each word to '{target}'? (smaller distance = more similar)\n")

    scores = []
    for word, vec in WORDS.items():
        if word == target:
            continue
        scores.append((word, distance(WORDS[target], vec)))

    scores.sort(key=lambda pair: pair[1])        # nearest first
    for word, dist in scores:
        print(f"  {target} <-> {word:6}  distance = {dist:.2f}")

    nearest = scores[0][0]
    print(f"\nClosest to '{target}': '{nearest}'  -> same 'corner' of meaning (both animals).")
    print("Notice: 'car' and 'truck' are far away -- different meaning, far on the map.")


if __name__ == "__main__":
    main()
