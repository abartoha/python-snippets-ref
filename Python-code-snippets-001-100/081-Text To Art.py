'''
81-Text To Art

pip install art==3.4

more info:
http://www.shaghighi.ir/art/
'''

from art import text2art, tprint

# Default.
print (text2art("default"))

# Boxed.
tprint("block",font="block",chr_ignore=True)

# Random.
print(text2art("random","rand"))
