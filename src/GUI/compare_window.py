from tkinter import ttk, BOTH
import numpy as np
from graph_window import graph_window
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import matplotlib.cm as cm

# TODO: DELETE ALL IMPORTs bellow
from tkinter import *
from tkinter import ttk
from menu_bar import *
from graph_window import *
from parameter_window import *
from transistors import Transistor
import numpy as np
import pandas as pd
from utils import updata_parameter_window, update_graph_window, calc_all_data_for_new_file


class CompareWindow():

    def __init__(self, root, transistorArray, chars_window) -> None:
        self.transistorsArray = transistorArray
        self.root = root
        self.mainFrame = ttk.Frame(self.root, padding="30 30 30 30")
        self.mainFrame.pack(fill=BOTH)
        self.chars_window = chars_window
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.checkButtonsArray = []
        self.create_checkboxes()

    def create_checkboxes(self):
        frame_label = ttk.Frame(self.mainFrame)
        frame_label.grid(column=1, row=0)
        main_label = Label(frame_label, text="Read files", font=("TkDefaultFont", 12, "bold"))
        main_label.grid(column=0, row=0)
        for i, transistor in enumerate(self.transistorsArray):
            var = IntVar()
            checkbutton = ttk.Checkbutton(self.mainFrame, variable=var, onvalue=1, offvalue=0, command=lambda i=i: self.checkbox_changed(i))
            checkbutton_label = Label(self.mainFrame, text=transistor.name)
            checkbutton.grid(column=1, row=i+1)
            checkbutton_label.grid(column=0, row=i+1)
            self.checkButtonsArray.append(var)

    def checkbox_changed(self, index):
        active_trans_array = []
        for checkbutton in self.checkButtonsArray:
            active_trans_array.append(checkbutton.get())

        self.chars_window.add_tabs(self.transistorsArray, active_trans_array)

    def change_transistors_array(self, transistor_array):
        self.transistorsArray = transistor_array
        self.create_checkboxes()

    def get_parameter_widget(self) -> ttk.Frame:
        return self.mainFrame


class CompareCharsWindow():

    def __init__(self, root):
        self.root = root
        # Create empty tab. Tabs with graphs will be created after the file is opened.
        self.tabControl = ttk.Notebook(root)
        emptyTab = ttk.Frame(self.tabControl)
        self.tabControl.add(emptyTab, text="Tab 1")
        self.tabControl.pack(expand=1, fill="both")
        ttk.Label(emptyTab, text="Check data to compare").pack(expand=True)

    def get_graph_widget(self) -> ttk.Notebook:
        return self.tabControl

    def add_tab(self, name: str, graphTitle: str, xLabel: str, yLabel: str, transistors_array, x_param, y_param, active_trans_array, log=False):
        newTab = ttk.Frame(self.tabControl)
        colors = cm.rainbow(np.linspace(0, 1, len(transistors_array)))
        fig = Figure(figsize=(5, 4), dpi=100)
        subplot = fig.add_subplot(111)
        for i in range(0, len(transistors_array)):
            if active_trans_array[i] == 1:
                xdata = getattr(transistors_array[i], x_param)
                ydata = getattr(transistors_array[i], y_param)
                if(log==True):
                    subplot.semilogy(xdata, ydata, label=transistors_array[i].name, color=colors[i])
                elif(log==False):
                    subplot.plot(xdata, ydata, label=transistors_array[i].name, color=colors[i])

        subplot.set_title(graphTitle)
        subplot.set_ylabel(yLabel)
        subplot.set_xlabel(xLabel)
        handles, labels = fig.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        subplot.legend(by_label.values(), by_label.keys())
        subplot.grid(which='minor', alpha=0.2)
        subplot.grid(which='major', alpha=0.5)
        subplot.minorticks_on()

        self.tabControl.add(newTab, text=name)

        canvas = FigureCanvasTkAgg(fig, master=newTab)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, newTab)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def add_tabs(self, transistor_array, active_trans_array):
        graphWindow.remove_all_tab()
        graphWindow.add_tab("Transfer characteristics", "Transfer characteristics", "Vgs [V]", "Ids [A]", transistor_array, "vgs", "ids_vgs", active_trans_array)
        graphWindow.add_tab("Transfer characteristics-log", "Transfer characteristics-log", "Vgs [V]", "Ids [A]", transistor_array, "vgs", "ids_vgs", active_trans_array, log=True)
        graphWindow.add_tab("Output characteristics", "Output characteristics", "Vds [V]", "Ids [A]", transistor_array, "i_vds", "i_ids_vds", active_trans_array)
        graphWindow.add_tab("gm", "gm", "Vgs [V]", "gm [S]", transistor_array , "xgm", "gm", active_trans_array)
        graphWindow.add_tab("gds", "gds", "Vds [V]", "gds [S]", transistor_array , "xgds", "gds", active_trans_array)

    def remove_all_tab(self):
        for i in range(0, len(self.tabControl.tabs())):
            self.tabControl.forget(0)

## EXAMPLE OF USE DONT USE THIS FILE SEPARATELY!

if __name__ == "__main__":

    root = Tk()
    root.title("ZPB FET")

    t_array = []
    t_array.append(calc_all_data_for_new_file("res/FET1.xlsx"))
    t_array.append(calc_all_data_for_new_file("res/FETs_1.xlsx"))
    t_array.append(calc_all_data_for_new_file("res/FETs_2.xlsx"))
    t_array.append(calc_all_data_for_new_file("res/FETs.xlsx"))

    # Create a paned window for displaying widgets
    pw = PanedWindow(orient='horizontal')
    # Insert display widgets into the paned window
    # Graph window
    graphWindow = CompareCharsWindow(pw)
    pw.add(graphWindow.get_graph_widget())

    # Parameters display
    parameterWindow = CompareWindow(pw, t_array, graphWindow)
    pw.add(parameterWindow.get_parameter_widget())
    # updata_parameter_window(parameterWindow, t)

    # Add a menu bar to the program window
    menu = Menu_bar(root, parameterWindow, graphWindow)
    root.config(menu=menu.get_menu_bar())

    pw.pack(fill=BOTH, expand=True)
    pw.configure(sashrelief=RAISED)

    root.mainloop()
