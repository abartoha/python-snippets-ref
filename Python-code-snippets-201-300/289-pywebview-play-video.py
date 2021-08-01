"""Code snippets vol-58
   289-pywebview-Play video.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requires:
---------
pip3 install pywebview
play_video.html file and test.mp4 in cwd.

Origin:
https://github.com/r0x0r/pywebview/tree/master/examples
"""
import webview

if __name__ == '__main__':
    master_window = webview.create_window('Pywebview: Play video example',
                                          url='play_video.html',
                                          width=625, height=460,
                                          confirm_close=True,)

webview.start()
