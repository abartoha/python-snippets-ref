"""Code snippets vol-58
   287-pywebview display text and image.

Requires:
pip3 install pywebview

display_txt_img.html
and model.jpg both in cwd.

Origin:
https://github.com/r0x0r/pywebview/tree/master/examples
"""
import webview

if __name__ == '__main__':
    master_window = webview.create_window('Pywebview-text and image example',
                                          url='display_txt_img.html',
                                          width=665, height=575,
                                          confirm_close=True,)

webview.start()
