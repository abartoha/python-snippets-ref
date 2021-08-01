"""Exit on window x
   stevepython.wordpress.com
   code-snippet-vol_41-snip_202
   Steve Shambles.
"""
from tkinter import Label, messagebox, Tk

root = Tk()
root.title('Click exit')

txt_label = Label(root, text='Click on this windows X to test.')
txt_label.grid()

def exit_prg():
    """Yes-no requestor to exit program."""
    ask_yn = messagebox.askyesno('Question',
                                 'Are you sure you want to quit?')
    if ask_yn is False:
        return
    root.destroy()

# This what checks for a click on the X.
root.protocol("WM_DELETE_WINDOW", exit_prg)

root.mainloop()
