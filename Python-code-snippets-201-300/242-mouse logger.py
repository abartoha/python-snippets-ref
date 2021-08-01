"""Code snippets vol-49-snippet-242
   mouse logger

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements:pip3 install pynput
https://pypi.org/project/pynput/

origin:
https://gist.github.com/brentvollebregt/6e53b013d36ff7be3cf146948c763a51
"""
import logging
from pynput.mouse import Listener

log_dir = ''

logging.basicConfig(filename=(log_dir + 'mouse_log.txt'),
                    level=logging.DEBUG,
                    format='["%(asctime)s", %(message)s]')

def on_click(x, y, button, pressed):
    """If mouse button clicked."""
    if pressed:
        logging.info('"{0}", {1}'.format(button, (x, y)))

def on_scroll(x, y, dx, dy):
    """If mouse scrolled."""
    logging.info('"{0}", {1}'.format('Button.scroll', (x, y)))

with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
