'''
Python Code Snippets #21
101-Using Tkinters internal bitmaps and cursors

Tested on Python V3.6x, Window 7
By Steve Shambles June 2019
'''
from tkinter import  Tk, Button, LabelFrame

ROOT = Tk()
ROOT.title('Buttons')

def clk_but():
    '''button was clicked'''
    print('clicked')

FRAME0 = LabelFrame(ROOT, text='Built in tk bitmaps')
FRAME0.grid(padx=10, pady=10)

BUT1 = Button(FRAME0, bitmap="info", cursor="exchange", command=clk_but)
BUT1.grid(pady=5, padx=5, row=0, column=0)

BUT2 = Button(FRAME0, bitmap="hourglass", cursor="pirate", command=clk_but)
BUT2.grid(pady=5, padx=5, row=0, column=1)

BUT3 = Button(FRAME0, bitmap="question", cursor="crosshair", command=clk_but)
BUT3.grid(pady=5, padx=5,  row=0, column=2)

BUT4 = Button(FRAME0, bitmap="error", cursor="heart", command=clk_but)
BUT4.grid(pady=5, padx=5,  row=0, column=3)

BUT5 = Button(FRAME0, bitmap="warning", cursor="hand1", command=clk_but)
BUT5.grid(pady=5, padx=5,  row=0, column=4)

BUT6 = Button(FRAME0, bitmap="gray75", cursor="sailboat", command=clk_but)
BUT6.grid(pady=5, padx=5,  row=1, column=0)

BUT7 = Button(FRAME0, bitmap="gray50", cursor="shuttle", command=clk_but)
BUT7.grid(pady=5, padx=5, row=1, column=1)

BUT8 = Button(FRAME0, bitmap="gray25", cursor="spraycan", command=clk_but)
BUT8.grid(pady=5, padx=5, row=1, column=2)

BUT8 = Button(FRAME0, bitmap="gray12", cursor="watch", command=clk_but)
BUT8.grid(pady=5, padx=5, row=1, column=3)


ROOT.mainloop()
