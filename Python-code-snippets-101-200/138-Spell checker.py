'''
Python code snippet
138-Spell Checker
stevepython.wordpress.com

pip3 install textblob

Source:
https://www.pythonprogramming.in/natural-language-processing-in-python/how-to-correct-spelling-using-textblob-in-python.html
'''
from textblob import TextBlob

# Text to spell check
data = "Natural language is a cantral part of our day to daay life,"  \
" and it's so intrestting to work on any prublem relayted to langagesy."
 
output = TextBlob(data).correct()
print()
print()
print(data)
print()
print("----------spelling checked and fixed--------------------")
print(output)
