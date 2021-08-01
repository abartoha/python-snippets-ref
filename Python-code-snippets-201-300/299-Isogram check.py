"""Code snippets vol-60
   299-Isogram test

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
None

Determine if a word or phrase is an isogram.
An isogram (also known as a "nonpattern word")
is a word or phrase without a repeating letter,
however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

    lumberjacks
    background
    downstream
    six-year-old

The word isograms, however, is not an isogram, because the s repeats.

origin:
https://codereview.stackexchange.com/questions/244414/exercism-determine-if-a-word-or-phrase-is-an-isogram
"""
from collections import Counter
import string


def is_isogram(word):
    """Check word to see if it is an Isogram."""
    char_counts = Counter(word.lower())
    return all(count == 1 for char, count in char_counts.items()
               if char in string.ascii_lowercase)


print(is_isogram("python"))

print(is_isogram("python code"))
