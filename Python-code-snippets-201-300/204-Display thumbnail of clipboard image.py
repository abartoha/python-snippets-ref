"""Display thumbnail of clipboard image.
stevepython.wordpress.com
code-snippet-vol_41-snip_204

By Steve Shambles

required:
pip3 install pillow
"""

from tkinter import Label, Tk
import webbrowser

from PIL import Image, ImageGrab, ImageTk

root = Tk()

def grab_cb_img():
    """Grab image from clipboard, create thumb and display with original"""
    img = ImageGrab.grabclipboard()
    if img is not None:
        # Save the image.
        img.save('cbimage.jpg')

        # Create frame for the image.
        img_frame = root
        img_frame.grid()
        img_frame.title('Thumbnail')
        img_frame.resizable(False, False)

        # Load back image.
        img = Image.open('cbimage.jpg')

        # Make a 256x256 thumbnail and display.
        img.thumbnail((256, 256), Image.ANTIALIAS)
        PHOTO = ImageTk.PhotoImage(img)
        la_bel = Label(img_frame, image=PHOTO)
        la_bel.img = PHOTO
        la_bel.grid()
        webbrowser.open('cbimage.jpg')
    else:
        root.destroy()
        print('No image found on clipboard.')

grab_cb_img()
