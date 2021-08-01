'''
116-Easygui buttonbox with image

pip3 install easygui

By Steve Shambles July 2019
Visit my blog for more snippets like this
stevepython.wordpress.com
'''
from easygui import buttonbox

image = "test.jpg"
msg = "Do you like this picture?"
choices = ["Yes", "No", "No opinion", "Hate it"]
reply = buttonbox(msg, image=image, choices=choices)

if reply == "Yes":
    print("Jen say's that's very kind of you to say so.")

if reply == "No":
    print("Okay, you are entitled to your incorrect opinion I guess.")

if reply == "No opinion":
    print("You just sit on the fence then, you schmuck.")

if reply == "Hate it":
    print("How dare you insult the lovely Jen.")
