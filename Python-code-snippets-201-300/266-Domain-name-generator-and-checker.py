"""Code snippets vol-54
   266-Domain Name generator and checker

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements: None

Origin:
https://gist.github.com/kid-on-github/f3137b995494a2a45d9ec7069506e074
https://stackoverflow.com/questions/12297500/python-module-for-nslookup
"""
import socket
import random

words = '''\
profile
info
swap
tag
me
meet
greet
tap
yes
friend
share
swap
connect
with
new
lets
go
run
pair
pear
join
net
network
time
tyme\
'''

# Turn the words string into an array.
words = words.split('\n')

combos = []
for i in words:

    for ii in words:
        combos.append(i+ii)

# Loop through the list in random order.
free = 0
while len(combos) > 0:
    ran = random.randint(0, len(combos)-1)
    name = combos.pop(ran) + '.com'

    try:
        ip_list = list({addr[-1][0] for addr in socket.getaddrinfo(name, 0, 0, 0, 0)})
    except:
        print(name)
        free += 1

print(free, 'domains free')
