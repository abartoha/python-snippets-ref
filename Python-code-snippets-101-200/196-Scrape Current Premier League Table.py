"""
Python code snippets vol 40.
196-Scrape Current Premier League Table.

By Steve Shambles Nov 2019, with help from r/learnpython/reddit.
stevepython.wordpress.com

pip install beautifulSoup4
pip install requests
"""
import datetime
import webbrowser

import requests
from bs4 import BeautifulSoup

# Get html of current PL table from sky.com.
r = requests.get('https://www.skysports.com/premier-league-table')
soup = BeautifulSoup(r.text, 'html.parser')
league_table = soup.find('table', class_='standing-table__table callfn')

# Get current date in human readable form.
current_date = datetime.date.today()
current_date = current_date.strftime("%d %B %Y")

# Set up the text headers in strings.
title_text = ' Premier League Table as of '+str(current_date)+'.\n Scraped from sky.com\n'
tab_head = '   Team                     Pl  W D  L  F  A GD Pts'

# Create a file name from current date.
file_name = str(current_date)+'.txt'

# Open a fresh text file in current directory, and save the header texts.
with open(file_name, 'w') as f:
    f.write(title_text)
    f.write('\n')
    f.write(tab_head)
    f.write('\n')

# For shell version, if required.
print(title_text)
print(tab_head)

# Do the scraping.
for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')

    for row in rows:
        rank = row.find_all('td', class_='standing-table__cell')[0].text
        pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name')
        pl_team = pl_team['data-long-name']
        games_played = row.find_all('td', class_='standing-table__cell')[2].text
        games_won = row.find_all('td', class_='standing-table__cell')[3].text
        games_drawn = row.find_all('td', class_='standing-table__cell')[4].text
        games_lost = row.find_all('td', class_='standing-table__cell')[5].text
        goals_for = row.find_all('td', class_='standing-table__cell')[6].text
        goals_against = row.find_all('td', class_='standing-table__cell')[7].text
        goal_diff = row.find_all('td', class_='standing-table__cell')[8].text
        total_points = row.find_all('td', class_='standing-table__cell')[9].text

        # Need 25 spaces after pl_team to format table for printing.
        space_pad = 25 - len(pl_team)
        pl_team = pl_team + ' ' * space_pad

        # If single figure, pad with a space to format table.
        if int(games_won) < 10:
            games_won = ' '+str(games_won)

        if int(games_drawn) < 10:
            games_drawn = ' '+str(games_drawn)

        if int(games_lost) < 10:
            games_lost = ' '+str(games_lost)

        if int(goals_for) < 10:
            goals_for = ' '+str(goals_for)

        if int(goals_against) < 10:
            goals_against = ' '+str(goals_against)

        if int(goal_diff) < 10 and int(goal_diff) >= 0:
            goal_diff = ' '+str(goal_diff)

        if int(rank) < 10:
            rank = ' '+str(rank)


        pl_table = str(rank)+' '+str(pl_team)+str(games_played)+' '  \
                   +str(games_won)+str(games_drawn)+' '+str(games_lost)  \
                   +' '+str(goals_for)+' '+str(goals_against)+' '  \
                   +str(goal_diff)+' '+str(total_points)

        # Print table in shell, if required.
        print(pl_table)

        # Append to the text file.
        with open(file_name, 'a') as f:
            f.write(pl_table)
            f.write('\n')

# Open and display the text file.
webbrowser.open(file_name)
