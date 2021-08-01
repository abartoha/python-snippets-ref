"""Code snippets vol-45-snippet-225
Split a book into seperate chapters as files.
Book needs to be converted to plain text first.

#tested and works on an adhd epub i found and converted to txt

stevepython.wordpress.com
Download all snippets so far:
https://wp.me/Pa5TU8-1yg

https://stackoverflow.com/questions/60141999/split-text-into-chapters-and-store-it-in-txt-files
"""
import re

# Here we open the book, in this case it is called book.txt.
book = open("bookv2.txt", "r")

# Assign book the value of book.txt, not just the location.
book = str(book.read())

# Finds all the chapter markers in the book and makes a list.
chapters = re.split("Chapter ", book, flags = re.IGNORECASE)

# Removes the first item in list as this is "".
chapters.pop(0)

# Loops for the number of chapters in the book.
for i in range(1, len(chapters)+1):

    # Opens a book with the name of i, if it does not exist, it creates one.
    writeBook = open("{}.txt".format(i), "w+")

    # Overwrites what is written in the book with the same chapter in the list.
    writeBook.write(chapters[i-1])
    # Finally, it closes the text file.
    writeBook.close()
