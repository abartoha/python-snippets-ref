'''
135-Password strength checker
stevepython.wordpresss.com

source:
https://codereview.stackexchange.com/questions/224525/checking-the-strength-of-a-password-using-regexes
'''

import re

pw_to_check = input('please enter the password to be checked:')

# feel free to add more special charcters to list if required
rules = [
    ('password is too short', r'.{8}'),
    ('password needs at least one lower case character', r'[a-z]'),
    ('password needs at least one upper case character', r'[A-Z]'),
    ('password needs at least one special character', r'[-_?!@#$%^&*£+=#*?]'),
    ('password needs at least one number', r'[0-9]'),
]

err_msg = '\n'.join(
    req
    for req, regex in rules
    if not re.search(regex, pw_to_check)
)

print(err_msg or 'password is ok')
