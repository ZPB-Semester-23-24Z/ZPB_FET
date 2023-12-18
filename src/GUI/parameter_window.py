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

        self.Ion = StringVar()
        self.Ioff = StringVar()
        self.Vt = StringVar()
        self.SS = StringVar()
        self.lamb = StringVar()
        self.mobility = StringVar()
        self.Ion.set(0.0)
        self.Ioff.set(0.0)
        self.Vt.set(0.0)
        self.SS.set(0.0)
        self.lamb.set(0.0)
        self.mobility.set(0.0)

        self.IonLabel = Label(self.mainFrame, text="Ion")
        self.IoffLabel = Label(self.mainFrame, text="Ioff")
        self.VtLabel = Label(self.mainFrame, text="Vt")
        self.SSLabel = Label(self.mainFrame, text="SS")
        self.lambdaLabel = Label(self.mainFrame, text="\u03BB")
        self.mobilityLabel = Label(self.mainFrame, text="\u03BDd")
        self.IonLabel.grid(column=1, row=1, sticky=W)
        self.IoffLabel.grid(column=1, row=2, sticky=W)
        self.VtLabel.grid(column=1, row=3, sticky=W)
        self.SSLabel.grid(column=1, row=4, sticky=W)
        self.lambdaLabel.grid(column=1, row=5, sticky=W)
        self.mobilityLabel.grid(column=1, row=6, sticky=W)

        self.IonValLabel = Label(self.mainFrame, textvariable=self.Ion)
        self.IoffValLabel = Label(self.mainFrame, textvariable=self.Ioff)
        self.VtValLabel = Label(self.mainFrame, textvariable=self.Vt)
        self.SSValLabel = Label(self.mainFrame, textvariable=self.SS)
        self.lambdaValLabel = Label(self.mainFrame, textvariable=self.lamb)
        self.mobilityValLabel = Label(self.mainFrame, textvariable=self.mobility)
        self.IonValLabel.grid(column=2, row=1, sticky=E)
        self.IoffValLabel.grid(column=2, row=2, sticky=E)
        self.VtValLabel.grid(column=2, row=3, sticky=E)
        self.SSValLabel.grid(column=2, row=4, sticky=E)
        self.lambdaValLabel.grid(column=2, row=5, sticky=E)
        self.mobilityValLabel.grid(column=2, row=6, sticky=E)
    def get_parameter_widget(self) -> ttk.Frame:
        return self.mainFrame
