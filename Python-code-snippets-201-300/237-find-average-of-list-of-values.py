"""Code snippets vol-48-snippet-237
   Find average value of numerical list

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements: None.

Origin:
https://pythonforundergradengineers.com/statistics-in-python-using-the-statistics-module.html
"""
from statistics import mean

TEST_SCORES = [60, 83, 83, 91, 100]

print(TEST_SCORES)
print('The average value is '+str(mean(TEST_SCORES)))
