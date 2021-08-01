"""Code snippets vol-47-snippet-233
   Get environment variables

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements: None.

Origin:
Steve Shambles March 2020
"""
import os

# Display some example environmental variables.
print(os.getenv('USERNAME'))
print(os.getenv('HOME'))
print(os.getenv('COMPUTERNAME'))
print(os.getenv('PROCESSOR_IDENTIFIER'))
print(os.getenv('PROCESSOR_ARCHITECTURE'))
print(os.getenv('OS'))

# Note these examples are Windows vars,
# except HOME, which is used on Linux too.
