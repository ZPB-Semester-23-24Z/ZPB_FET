from tkinter import *
from tkinter import ttk

class parameter_window:
    def __init__(self, root):
        self.root = root
        self.mainFrame = ttk.Frame(root, padding="30 30 30 30")
        #self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainFrame.pack(fill=BOTH)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        initval=0.0
        self.Ion = StringVar()
        self.Ioff = StringVar()
        self.Vt = StringVar()
        self.SS = StringVar()
        self.lamb = StringVar()
        #self.mobility = StringVar()
        self.Ion.set(f'{initval:e}')
        self.Ioff.set(f'{initval:e}')
        self.Vt.set(f'{initval:e}')
        self.SS.set(f'{initval:e}')
        self.lamb.set(f'{initval:e}')
        #self.mobility.set(f'{initval:e}')

        self.IonLabel = Label(self.mainFrame, text="Ion")
        self.IoffLabel = Label(self.mainFrame, text="Ioff")
        self.VtLabel = Label(self.mainFrame, text="Vt")
        self.SSLabel = Label(self.mainFrame, text="SS")
        self.lambdaLabel = Label(self.mainFrame, text="\u03BB")
        #self.mobilityLabel = Label(self.mainFrame, text="\u03BDd")
        self.IonLabel.grid(column=1, row=1, sticky=W)
        self.IoffLabel.grid(column=1, row=2, sticky=W)
        self.VtLabel.grid(column=1, row=3, sticky=W)
        self.SSLabel.grid(column=1, row=4, sticky=W)
        self.lambdaLabel.grid(column=1, row=5, sticky=W)
        #self.mobilityLabel.grid(column=1, row=6, sticky=W)

        variableLabelWidth = 10
        variableLabelpadx = 5
        self.IonValLabel = Label(self.mainFrame, textvariable=self.Ion, borderwidth=3, relief="sunken", width=variableLabelWidth)
        self.IoffValLabel = Label(self.mainFrame, textvariable=self.Ioff, borderwidth=3, relief="sunken", width=variableLabelWidth)
        self.VtValLabel = Label(self.mainFrame, textvariable=self.Vt, borderwidth=3, relief="sunken", width=variableLabelWidth)
        self.SSValLabel = Label(self.mainFrame, textvariable=self.SS, borderwidth=3, relief="sunken", width=variableLabelWidth)
        self.lambdaValLabel = Label(self.mainFrame, textvariable=self.lamb, borderwidth=3, relief="sunken", width=variableLabelWidth)
        #self.mobilityValLabel = Label(self.mainFrame, textvariable=self.mobility, borderwidth=3, relief="sunken", width=variableLabelWidth)
        self.IonValLabel.grid(column=2, row=1, sticky=E, pady=10, padx=variableLabelpadx)
        self.IoffValLabel.grid(column=2, row=2, sticky=E, pady=10, padx=variableLabelpadx)
        self.VtValLabel.grid(column=2, row=3, sticky=E, pady=10, padx=variableLabelpadx)
        self.SSValLabel.grid(column=2, row=4, sticky=E, pady=10, padx=variableLabelpadx)
        self.lambdaValLabel.grid(column=2, row=5, sticky=E, pady=10, padx=variableLabelpadx)
        #self.mobilityValLabel.grid(column=2, row=6, sticky=E, pady=10, padx=variableLabelpadx)

        self.IonUintLabel = Label(self.mainFrame, text="A")
        self.IoffUintLabel = Label(self.mainFrame, text="A")
        self.VtUintLabel = Label(self.mainFrame, text="V")
        self.SSUintLabel = Label(self.mainFrame, text="V/dec")
        self.lambdaUintLabel = Label(self.mainFrame, text=" ")
        #self.mobilityUintLabel = Label(self.mainFrame, text="cm2/(V⋅s)")
        self.IonUintLabel.grid(column=3, row=1, sticky=W)
        self.IoffUintLabel.grid(column=3, row=2, sticky=W)
        self.VtUintLabel.grid(column=3, row=3, sticky=W)
        self.SSUintLabel.grid(column=3, row=4, sticky=W)
        self.lambdaUintLabel.grid(column=3, row=5, sticky=W)
        #self.mobilityUintLabel.grid(column=3, row=6, sticky=W)
    def get_parameter_widget(self) -> ttk.Frame:
        return self.mainFrame

    def set_Ion(self, val):
        self.Ion.set(f'{val:e}')

    def set_Ioff(self, val):
        self.Ioff.set(f'{val:e}')

    def set_Vt(self, val):
        self.Vt.set(f'{val:e}')

    def set_SS(self, val):
        self.SS.set(f'{val:e}')

    def set_lambda(self, val):
        self.lamb.set(f'{val:e}')

    def set_mobility(self, val):
        self.mobility.set(f'{val:e}')