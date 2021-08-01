"""
Python code snippets vol 40.
198-Hex To RGB Conversion
stevepython.wordpress.com

source:
https://gist.github.com/matthewkremer/3295567
"""

def hex_to_rgb(hex):
     hex = hex.lstrip('#')
     hlen = len(hex)
     return tuple(int(hex[i:i+hlen//3], 16) for i in range(0, hlen, hlen//3))

print(hex_to_rgb('F8CA'))
