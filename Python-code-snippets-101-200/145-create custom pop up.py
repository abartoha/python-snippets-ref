'''
145-Create a custom pop up box
more python code snippets:
stevepython.wordpress.com

source: Steve Shambles
pip installs none
'''

import tkinter as tk

root = tk.Tk()
root.title('Your main program window')
top = tk.Toplevel(root)
top.title ("Custom msgbox")

def btn_clk():
    print('clicked button')


lbl = tk.Label(top, fg="blue",
               text="This is an example of a custom pop up box.\n"
               "You can add almost any feature you can think of.")
lbl.pack()

btn = tk.Button(top, bg="darkgreen", fg="white", text='Click Me', command=btn_clk)
btn.pack()

root.mainloop()
