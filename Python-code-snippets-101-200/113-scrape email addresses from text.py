import os
import re

# vars for filenames
filename = 'test.txt'
newfilename = 'emails.txt'

# read file
data = open(filename,'r')
bulkemails = data.read()


# regex = whoEver@wHerever.xxx
r = re.compile(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)')
results = r.findall(bulkemails)

emails = ""
for x in results:
	emails += str(x)+"\n"
print(emails)


f = open(newfilename, 'w')
f.write(emails)
f.close()
print ("File written.")
