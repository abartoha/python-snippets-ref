"""Code snippets vol-59
   294-Print permutations of a given string

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
None

origin:
https://gist.github.com/accakks/fbf2383ce782bbf089c68a807695b3e1
"""
from itertools import permutations


def print_permutations(s):
    """Prints permutations of a given string"""
    ans = list(permutations(s))
    cnt = 1
    for permutation in ans:
        print(str().join(permutation) + "\n" + str(cnt), end=" ")
        cnt += 1


s = input('Enter input string\n')
print_permutations(s)
