"""Code snippets vol-57
   284-Check string for a pangram

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
None

original code here:
https://gist.github.com/Allwin12/4f8d9d8066adc838558a22949ba400c0
"""
import string

alphabets = string.ascii_lowercase


def test_pangram(sentence, alphabets):
    for char in alphabets:
        if char not in sentence.lower():
            return False
    return True


text_string = 'the quick brown fox jumps over a lazy dog'
print()

if test_pangram(text_string, alphabets):
    print(text_string, '\nis a pangram because it contains every letter of '
          'the alphabet exactly once.')
else:
    print(text_string, '\nis not a pangram. A pangram has to contain every '
          'letter of the alphabet exactly once.')
