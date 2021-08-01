"""Code snippets vol-59
   293-Auto Clipboard Saver.
   Windows only.
   By Steve Shambles. June 2020

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip3 install Pillow
pip3 install pyperclip

Origin:
https://stevepython.wordpress.com/2020/03/10/detect-clipboard-text-and-images
"""
from datetime import datetime
import os
from threading import Timer
import winsound

from PIL import ImageGrab
import pyperclip


# Check image folder exists in current directory.
IMG_FOLDER = 'clipboard_images'
check_IMG_FOLDER = os.path.isdir(IMG_FOLDER)
if not check_IMG_FOLDER:
    os.makedirs(IMG_FOLDER)

# Check text folder exists in current directory.
TXT_FOLDER = 'clipboard_texts'
check_TXT_FOLDER = os.path.isdir(TXT_FOLDER)
if not check_TXT_FOLDER:
    os.makedirs(TXT_FOLDER)


def beep_sound():
    """Beep sound. frequency, duration."""
    winsound.Beep(840, 100)


def create_filename():
    """I wanted a properly unique and readable date and time as
       the file name."""
    global time_stamp
    time_stamp = (datetime.now().strftime(r'%d' + ('-') + '%b' + ('-')
                                          + '%Y' + ('-') + '%H' + ('.')
                                          + '%M' + ('-') + '%S' + 's'))
    return time_stamp


def save_cb_text():
    """If text found on clipboard, Save to uniquely named text file."""
    # Grab clipboard contents.
    cb_txt = pyperclip.paste()

    if cb_txt:
        tits = '-' * 34 + '\n'
        create_filename()
        file_name = time_stamp+'.txt'
        folder = r'clipboard_texts/'

        with open(folder+str(file_name), 'w') as contents:
            contents.write('Clipboard text found: '+str(time_stamp)+'\n')
            contents.write(tits)
            contents.write(cb_txt)
            beep_sound()

            print('Clipboard text found and saved as', file_name)
            # Clear clipboard.
            pyperclip.copy('')



def grab_cb_img():
    """If image found, Save to uniquely named jpg file."""
    # Grab clipboard.
    img = ImageGrab.grabclipboard()

    # If an image is found on the clipboard...
    if img:
        create_filename()
        file_name = time_stamp+'.jpg'
        folder = r'clipboard_images/'
        img.save(folder+file_name)
        beep_sound()
        print('Clipboard image found and saved as', file_name)

        # Clear clipboard so that same image is not saved again.
        pyperclip.copy('')


def main():
    """Main loop using 1 second timer to check clipboard."""
    grab_cb_img()
    save_cb_text()

    grab_timer = Timer(1, main)
    grab_timer.start()


main()
