"""Code snippets vol-52
   258-Multi-platform system Notification.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg

   Blog: stevepython.wordpress.com

requirements:
pip3 install plyer
https://pypi.org/project/plyer/


Origin:
https://plyer.readthedocs.io/en/latest/#plyer.facades.Notification
"""
from plyer import notification

notification.notify(
    title='Python in 2020                    ',
    message='What a great time to be alive!  ',
    timeout=7,
    toast=True,
    app_icon="python.ico",
    )

# Ignore, comment out, or replace app_icon line if you don't have the icon.
