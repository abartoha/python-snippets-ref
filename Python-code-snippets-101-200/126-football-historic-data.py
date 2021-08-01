'''
Snippet #126-View historic football data.
stevepython.wordpress.com

Tested on Win 7 and Linux Mint 19.1

source:unkown.

source of data:
https://www.football-data.co.uk/data.php

csv is part of python's standard library,
so you don't need to install it
'''

import csv

csv_file = csv.reader(open('pl-2018-2019-data.csv'))
next(csv_file)

for game in csv_file:
	home_team = game[2]
	away_team = game[3]

	home_goals = int(game[4])
	away_goals = int(game[5])

	home_odds = float(game[23])
	draw_odds = float(game[24])
	away_odds = float(game[25])
	print(home_team, "V", away_team, "score ", home_goals, "-", away_goals, ": Odds", home_odds)

