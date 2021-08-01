"""Code snippets vol-58
   286-pywebview-simple-webbrowser

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip3 install pywebview

origin:
https://github.com/r0x0r/pywebview/blob/master/examples/simple_browser.py
"""
import webview

if __name__ == '__main__':
    window = webview.create_window('Simple browser',
                                   'https://wp.me/paARwp-ax')
    webview.start()
