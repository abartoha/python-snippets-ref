"""Code snippets vol-59
   295-Tribal Wars Farm Helper
   tribalwars.co.uk
   tribalwars.net

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

requirements:
Windows Only.

pip3 install pyperclip

A text file saved in the current dir named farm.txt
containing the co-ords of each village to be farmed
on a seperate line each.

Origin:
Steve Shambles

Instructions:
After preparing your farm.txt file
Open your rally point in the game
run this script
and after each beep, enter troops to send,
paste in co-rds, then click attack.
repeat after each beep.
When you hear a double beep the farms have all been
sent out.

This will speed up non-premium farming a little,
but more importantly it saves you a lot of screen swapping
and copying co-ords to clipboard, it probably saved
me getting repetitive strain injury in my wrist.

I've never asked if this is legal in the game, but
I can't see why it wouldn't be. If they banned this
health saving script I'd quit the game for good.
"""
import time
import winsound

import pyperclip


co_ords = []
# Give a chance to set up rally pint trops for first go.
time.sleep(10)

# Open farm.txt and read all co-ords into a list.
with open('farm.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        co_ords.append(currentPlace)

farms = len(co_ords)
print(farms, "farms")

for a in range(farms):
    get_cords = co_ords[a]
    pyperclip.copy(get_cords)
    print(a, get_cords)
    winsound.Beep(840, 100)
    time.sleep(10)  # Change this to suit your speed needs.

pyperclip.copy("finished")
winsound.Beep(840, 100)
winsound.Beep(840, 100)
print("finished")
