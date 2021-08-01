"""Code snippets vol-53
   261-Wikipedia geo search.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg

   Blog: stevepython.wordpress.com

Requirements:
pip3 install wikipedia
https://pypi.org/project/wikipedia/

Origin: Unknown (sorry, had this on my drive for ages with no origin.)
"""
import wikipedia

print(wikipedia.geosearch(51.505905, -0.022066))

#returns:
#['Cabot Square', 'West India Quay', 'Canary Wharf',
#'International Sugar Organization', 'SS Robin',
#'Canary Wharf DLR station', '1 Cabot Square',
#'1 West India Quay', '25 North Colonnade', 'Marriott Canary Wharf']
