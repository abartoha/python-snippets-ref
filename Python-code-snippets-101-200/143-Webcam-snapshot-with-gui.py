'''
143-webcam-snapshot-with-gui

sources, vars+
https://kieleth.blogspot.com/2014/05/webcam-with-opencv-and-tkinter.html
'''
import datetime
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk
import cv2

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root.title("Tk WebCam Snapper")
lmain = tk.Label(root)
lmain.pack()

def show_frame():
    '''Main loop, display webcam capture'''
    global img
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

def snapshot():
    '''Take snapshot and save it to the file'''
    global img
    ts = datetime.datetime.now() # grab the current timestamp
    filename = "{}.jpg".format(ts.strftime("%d-%m-%Y-%H-%M-%S")) # filename

    img.save(filename, "JPEG")  # save image

    msg = "Snapshot Saved as:\n"+str(filename)
    messagebox.showinfo('Info', msg)

def destructor():
    '''Destroy the root object and release all resources'''
    root.destroy()
    cap.release()

# Buttons
btn_snap = tk.Button(root, text="Snapshot!", command=snapshot)
btn_snap.pack(fill="both", expand=True, padx=10, pady=10)

btn_quit = tk.Button(root, text="Quit", command=destructor)
btn_quit.pack(padx=10, pady=10)

show_frame()

root.mainloop()
