"""Remove parts of window frame

stevepython.wordpress.com
code-snippet-vol_42-snip_208

Source: Various
"""

from tkinter import Label, Tk

root = Tk()

# This removes the maximize button.
#root.resizable(0,0)

# This makes a window frame with no title or icon.
root.overrideredirect(1) # Close Python shell to quit this one.

# No maximize or minimize icons.
# This one does not work on Linux Mint 19.1
#root.attributes("-toolwindow", 1)

txt_label = Label(root, bg='powderblue',
                  text='This is some test text.')
txt_label.grid()

root.mainloop()
