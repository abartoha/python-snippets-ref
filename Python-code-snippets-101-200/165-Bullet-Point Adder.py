'''
Python code snippets vol 33:
165-Bullet-point Adder
Adds bullets to a copied string and sends it back to clipboard

pip3 install pyperclip

Source:
https://old.reddit.com/r/learnpython/comments/devvc2/
please_review_my_code_working_on_reducing_the/

'''
import pyperclip

clpbrd_source = pyperclip.paste().split('\n')

bulleted_result = "\n".join(list(map(lambda x: '* '+x, clpbrd_source)))

pyperclip.copy(bulleted_result)
