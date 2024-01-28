from tkinter import ttk, BOTH
import numpy as np

class compare_window():

    def __init__(self, root, transistor_array) -> None:
        self.transistors_array = transistor_array
        self.root = root
        self.mainFrame = ttk.Frame(self.root, padding="30 30 30 30")
        self.mainFrame.pack(fill=BOTH)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

    def change_transistors_array(self, transistor_array):
        self.transistors_array = transistor_array