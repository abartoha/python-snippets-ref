"""Autocomplete demo.

stevepython.wordpress.com
code-snippet-vol_41-snip_205

source:
https://gist.github.com/uroshekic/11078820

Few small improvements, Steve Shambles.
"""
import re
from tkinter import ACTIVE, END, Entry, Listbox, StringVar, Tk

class AutocompleteEntry(Entry):
    def __init__(self, autocompleteList, *args, **kwargs):

        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*',
                                     re.IGNORECASE)
                return re.match(pattern, acListEntry)

            self.matchesFunction = matches


        Entry.__init__(self, *args, **kwargs)
        self.focus()

        self.autocompleteList = autocompleteList

        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)

        self.listboxUp = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(width=self["width"],
                                           height=self.listboxLength)
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    self.listbox.place(x=self.winfo_x(),
                                       y=self.winfo_y() + self.winfo_height())
                    self.listboxUp = True

                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END,w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False

    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(ACTIVE))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)

    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != '0':
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)

                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != END:
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)

                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def comparison(self):
        return [ w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w) ]

if __name__ == '__main__':
    autocompleteList =[ 'Dora Lyons (7714)', 'Hannah Golden (6010)',
                        'Walker Burns (9390)', 'Dieter Pearson (6347)',
                        'Allen Sullivan (9781)', 'Warren Sullivan (3094)',
                        'Genevieve Mayo (8427)', 'Igor Conner (4740)',
                        'Ulysses Shepherd (8116)', 'Imogene Bullock (6736)',
                        'Dominique Sanchez (949)', 'Sean Robinson (3784)',
                        'Diana Greer (2385)', 'Arsenio Conrad (2891)',
                        'Sophia Rowland (5713)', 'Garrett Lindsay (5760)',
                        'Lacy Henry (4350)', 'Tanek Conley (9054)',
                        'Octavia Michael (5040)', 'Kimberly Chan (1989)',
                        'Melodie Wooten (7753)', 'Winter Beard (3896)',
                        'Callum Schultz (7762)', 'Prescott Silva (3736)',
                        'Adena Crane (6684)', 'Ocean Schroeder (2354)',
                        'Aspen Blevins (8588)', 'Allegra Gould (7323)',
                        'Penelope Aguirre (7639)', 'Deanna Norman (1963)',
                        'Herman Mcintosh (1776)', 'August Hansen (547)',
                        'Oscar Sanford (2333)', 'Guy Vincent (1656)',
                        'Indigo Frye (3236)', 'Angelica Vargas (1697)',
                        'Bevis Blair (4354)', 'Trevor Wilkinson (7067)',
                        'Kameko Lloyd (2660)', 'Giselle Gaines (9103)',
                        'Phyllis Bowers (6661)', 'Patrick Rowe (2615)',
                        'Cheyenne Manning (1743)', 'Jolie Carney (6741)',
                        'Joel Faulkner (6224)', 'Anika Bennett (9298)',
                        'Clayton Cherry (3687)', 'Shellie Stevenson (6100)',
                        'Marah Odonnell (3115)', 'Quintessa Wallace (5241)',
                        'Jayme Ramsey (8337)', 'Kyle Collier (8284)',
                        'Jameson Doyle (9258)', 'Rigel Blake (2124)',
                        'Joan Smith (3633)', 'Autumn Osborne (5180)',
                        'Renee Randolph (3100)', 'Fallon England (6976)',
                        'Fallon Jefferson (6807)', 'Kevyn Koch (9429)',
                        'Paki Mckay (504)', 'Connor Pitts (1966)',
                        'Rebecca Coffey (4975)', 'Jordan Morrow (1772)',
                        'Teegan Snider (5808)', 'Tatyana Cunningham (7691)',
                        'Owen Holloway (6814)', 'Desiree Delaney (272)',
                        'Armand Snider (8511)', 'Wallace Molina (4302)',]

    def matches(fieldValue, acListEntry):
        pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
        return re.match(pattern, acListEntry)

    root = Tk()
    root.title('Autocomplete Demo')
    root.geometry('300x200')

    entry = AutocompleteEntry(autocompleteList, root, listboxLength=6,
                              width=32, matchesFunction=matches)
    entry.grid(row=0, column=0)

    root.mainloop()
