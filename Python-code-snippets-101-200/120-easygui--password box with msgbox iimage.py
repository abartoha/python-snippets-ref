'''
117-Easygui password entry box and msgbox with image.

pip3 install easygui

By Steve Shambles July 2019
Visit my blog for more snippets like this
stevepython.wordpress.com
'''

from easygui import msgbox, passwordbox

title = "Password"
pass_word = (passwordbox("Please enter your password",title))

msgbox("Your password is: %s"%pass_word, title="Password revealed",
       image="thanks.jpg")
