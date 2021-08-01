"""Code snippets vol-44-snip-219
219-Print partial credit card number
stevepython.wordpress.com

possible uses to show part of credit card as a reminder
or modify for phone number.

Download 200+ no nonsense python code snippets:
https://wp.me/Pa5TU8-1yg

based on code from:
https://dev.to/bagadia/random-python-tricks-for-random-moods-4g82
"""

# Credit card number.
cc_nmbr = '1234 5678 9012 3456'

# Construct string.
show_nmbr = 'XXXX XXXX XXXX '+ cc_nmbr[-4:]

print(show_nmbr)
