"""Code snippets vol-58
   290-pywebview-Display image from url using internal html.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requires:
---------
pip3 install pywebview

Origin:
https://github.com/r0x0r/pywebview/tree/master/examples
"""
import webview

html = """
<html>
    <head>
    <style>
     body {color: blue;}
</style>
    <h3><center>Display text, get image from url, using internal html</center></h3>
    </head>
    <body>
    <center>
    <img src="https://stevepython.files.wordpress.com/2020/05/jacks-win.png">
    </center>
    </body>
</html>
"""

if __name__ == '__main__':
    master_window = webview.create_window('Pywebview-text and image example 2',
                                          html=html,
                                          width=600, height=700,
                                          confirm_close=True,)

webview.start()
