'''
Python Code Snippets #22
109-Validate email address

Tested on Python V3.6x, Window 7

pip3 install lepl

source:
http://code.activestate.com/recipes/
65215-e-mail-address-validation/?in=user-114221
'''
from lepl.apps.rfc3696 import Email
#Email function does not take an argument, it is just a validator

t1 = Email()

if t1('bollo@tesco.co.uk'):
    print("Looks like a valid Email address")
else:
    print("Appears to be an invalid Email address")
