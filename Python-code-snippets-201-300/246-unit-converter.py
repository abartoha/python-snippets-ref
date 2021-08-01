"""246-Unit Converter GUI

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements: None.

origin:
https://codereview.stackexchange.com/questions/239821/simple-gui-unit-converter-with-tkinter

Code has been Shamblized a bit to make it slightly more PEP8.
"""
from tkinter import Button, END, Entry, Label, Listbox, NE
from tkinter import Scrollbar, SE, StringVar, Tk

window = Tk()
window.title('Basic Converter')
window.geometry('500x300+500+350')

measurement1 = ''
measurement2 = ''

def convert_SI(val, unit_in, unit_out):
    """Based on unitconverters.net."""
    SI = {'Meter':1, 'Kilometer':1000, 'Centimeter':0.01, 'Millimeter':0.001,
          'Micrometer':0.000001, 'Mile':1609.35, 'Yard':0.9144, 'Foot':0.3048,
          'Inch':0.0254}
    return val*SI[unit_in]/SI[unit_out]

def selectedInput():
    """Whatever is currently selected."""
    global measurement1
    measurement1 = listbox.get(listbox.curselection())

def selectedOutput():
    """Whatever is currently selected."""
    global measurement2
    measurement2 = listbox1.get(listbox1.curselection())

def converter():
    """Do the coversation."""
    try:
        global measurement1, measurement2
        result.set(str(convert_SI(float(inputEntry.get()),
                                  measurement1, measurement2)))
    except:
        result.set('Error')

title = Label(window, text='Basic Converter', font='Calibri 16')
title.grid(columnspan=3)

result = StringVar()

# Input and output entry fields.
inputEntry = Entry(window)
inputEntry.grid(row=1, column=0)

arrow = Label(window, text='--->', font='Calibri 20')
arrow.grid(row=1, column=1)

outputEntry = Entry(window, textvariable=result)
outputEntry.grid(row=1, column=2)

convertButton = Button(window, text='Convert!', command=converter)
convertButton.grid(row=2, column=1)

scrollbar = Scrollbar(window)   #left scrollbar
scrollbar.grid(row=2, column=0, sticky=NE + SE)

listbox = Listbox(window, exportselection=False)   # Left listbox.
# exportselection option in order to select 2 different listbox at same time.
listbox.grid(row=2, column=0)

measurement_list = ['Meter', 'Kilometer', 'Centimeter', 'Millimeter',
                    'Micrometer', 'Mile', 'Yard', 'Foot', 'Inch']

for measurement in measurement_list:
    listbox.insert(END, measurement)

listbox.bind('<<ListboxSelect>>', lambda x: selectedInput())

# Attach listbox to scrollbar.
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Right scrollbar.
scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=2, column=2, sticky=NE + SE)
listbox1 = Listbox(window, exportselection=False) # Right listbox.
listbox1.grid(row=2, column=2)

for measurement in measurement_list:
    listbox1.insert(END, measurement)

listbox1.bind('<<ListboxSelect>>', lambda x: selectedOutput())
listbox1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=listbox1.yview)

# Configure grid layout to adjust whenever window dimensions change.
for i in range(3):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
