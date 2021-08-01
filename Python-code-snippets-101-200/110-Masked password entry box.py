'''
Python Code Snippets #22
110-Masked password entry box

Tested on Python V3.6x, Window 7

pip3 install pyautogui

source:
https://pyautogui.readthedocs.io/en/latest/msgbox.html
'''
import pyautogui

pass_word = pyautogui.password(text='Please enter your password',  \
title='Pyautogui password entry box', default='', mask='*')

print(pass_word)
