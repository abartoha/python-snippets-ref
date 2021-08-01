"""Code snippets vol-58
   Pywebview-Play mp3

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requires:
---------
pip3 install pywebview
play_mp3.html file and test.mp3 in cwd.

Origin:
https://github.com/r0x0r/pywebview/tree/master/examples
"""
import webview

if __name__ == '__main__':
    master_window = webview.create_window('Pywebview: Play mp3 example',
                                          url='play_mp3.html',
                                          resizable=False,
                                          width=565, height=128,
                                          confirm_close=True,)

webview.start()
