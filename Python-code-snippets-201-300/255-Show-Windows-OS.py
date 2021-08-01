"""Code snippets vol-51
   Snippet 255-Show Windows OS being used.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements:
pip3 install wmi
Windows only.

Origin:
http://timgolden.me.uk/python/wmi/tutorial.html
"""
import wmi

c = wmi.WMI()
for os in c.Win32_OperatingSystem():
    print(os.Caption)
