'''
Get random images from 4chan
pip3 install requests
IMPORTANT
Don't remove the time.sleeps as must comply with 4chan's API rules.
'''

import random
import time
import webbrowser
from functools import lru_cache

import requests

boards = ['a', 'c', 'w', 'm', 'cgl', 'cm', 'n', 'jp', 'vp',  \
          'v', 'vg','vr', 'co', 'g', 'tv', 'k', 'o', 'an',  \
          'tg','sp', 'asp','sci', 'int', 'out', 'toy', 'biz',  \
          'i', 'po', 'p', 'ck','ic', 'wg', 'mu', 'fa', '3',  \
          'gd','diy', 'wsg', 's', 'hc','hm', 'h', 'e', 'u',  \
          'd', 'y', 't', 'hr', 'gif', 'trv','fit', 'x', 'lit',  \
          'adv','lgbt', 'mlp', 'b', 'r', 'r9k','pol', 'soc',  \
          's4s']


def api(path):
    time.sleep(1.5)
    return requests.get(f'http://a.4cdn.org/{path}.json').json()


@lru_cache()
def board_data(board):
    return api(board + '/catalog')


def r4chan():
    """
    Returns [ random image URL, random image's thread URL ]
    """
    board = random.choice(boards)

    thread = random.choice([
        thread['no']
        for page in board_data(board)
        for thread in page["threads"]
    ])

    image = random.choice([
        f"{post['tim']}{post['ext']}"
        for post in api(f'{board}/thread/{thread}')['posts']
        if 'tim' in post
    ])

    return (
        f'https://is2.4chan.org/{board}/{image}',
        f'https://boards.4chan.org/{board}/thread/{thread}',
    )


# Opens x amount of image URLs in web browser
def main(numberOfImages):
    for i in range(numberOfImages):
        image_url, thread = r4chan()
        webbrowser.open(image_url)
        print(thread)

# change the 10 to how many images you require
main(10)
