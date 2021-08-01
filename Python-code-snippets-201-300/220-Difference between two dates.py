"""Code snippets vol-44-snip-220
220-Difference between two dates

stevepython.wordpress.com

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Requirements:
None

source:
https://gist.github.com/amalgjose/c767a4846d6ecaa3b6d7
"""
from datetime import datetime
from dateutil import relativedelta

##Aug 7 1989 8:10 pm
date_1 = datetime(1989, 8, 7, 20, 10)

##Dec 5 1990 5:20 am
date_2 = datetime(1990, 12, 5, 5, 20)

#This will find the difference between the two dates
difference = relativedelta.relativedelta(date_2, date_1)

years = difference.years
months = difference.months
days = difference.days
hours = difference.hours
minutes = difference.minutes
print()
print(date_1, ' and ', date_2)
print("Difference is %s year, %s months, %s days, %s hours, %s minutes "
      %(years, months, days, hours, minutes))
