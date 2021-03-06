'''
62-Sort Names By Surname
    Sort a list of names by surname in one line, using lambda.

    Borrowed from this blog:
    https://chrisalbon.com/python/basics/

    Made slightly amusing, and palatable for beginners by:
    Steve Shambles March 2019

    More Python atrocities at:
    https://stevepython.wordpress.com/
'''

# A list of names, could be loaded from a file,
# or inserted like this:
some_names = ["Steven Toast", "Ray Purchase", "Jane Plough",  \
"Susan Random", "Clem Fandango", "Clancy Moped"]

# Sort names by surname.
# This works by splitting the string at the space,
# and taking the last element, [-1],
# which the sort routines works on.

print(sorted(some_names, key=lambda x: x.split(" ")[-1]))
