"""Code snippets vol-52
   260-Filter a list of items.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg

   Blog: stevepython.wordpress.com

requirements:
None.

Origin:
https://www.poftut.com/how-to-filter-python-list-dictionary-array-string-list-object-tutorial-with-examples/
"""

names = ["sofa", "chair", "window", "lamp", "desk"]

# Filter out all items that contain the letter a.
filtered_names = filter(lambda item: 'a' not in item, names)
# Remove the 'not' part of 'not in' to filter in all names containg 'a'.

for item in filtered_names:
    print(item)
