"""Resize window image on the fly

stevepython.wordpress.com
code-snippet-vol_42-snip_207

pip install Pillow

Source:
https://stackoverflow.com/questions/24061099/tkinter-resize-background-image-to-window-size
"""

from tkinter import BOTH, Tk, YES
from tkinter import ttk

from PIL import Image, ImageTk

root = Tk()
root.title("Title")
root.geometry('640x480') # Comment this line out for interesting effect.

def resize_image(event):
    """Dynamically resize window containing image."""
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

image = Image.open('test.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo)

label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)

root.mainloop()
