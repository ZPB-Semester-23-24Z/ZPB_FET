from tkinter import *
from tkinter import ttk
import matplotlib


matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class graph_window:

    def __init__(self, root):
        self.root = root
        # Create empty tab. Tabs with graphs will be created after file is opened.
        self.tabControl = ttk.Notebook(root)
        self.create_empty_plot(800, 600)

    def create_empty_plot(self, width, height):
        graphWindow = ttk.Frame(self.tabControl)
        self.tabControl.add(graphWindow, text="Open data file")

        fig = Figure(figsize=(width / 100, height / 100), dpi=100)
        subplot = fig.add_subplot(111)

        subplot.text(0.5, 0.5, "Open data file", ha='center', va='center', fontsize=14, color='gray')
        subplot.grid(which='minor',alpha=0.2)
        subplot.grid(which='major',alpha=0.5)
        subplot.minorticks_on()

        canvas = FigureCanvasTkAgg(fig, master=graphWindow)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill='both', expand=1)

    def get_graph_widget(self) -> ttk.Notebook:
        """
        get_graph_widget This function returns created graph widget connected to this class.
        :return: Graph window widget. Type: ttk.Notebook
        """
        return self.tabControl

    def add_tab(self, name: str, graphTitle: str, xLabel: str, yLabel: str, xdata, ydata,log=False):
        """
        add_tab This function adds new tab to the graph window on the rightmost position.
        :param name: Name displayed on the tab in the graph window.
        :param graphTitle: Title displayed above the graph.
        :param xLabel: Label of the X axis
        :param yLabel: Label of the Y axis
        :param xdata: Array of numbers to be displayed on the X axis.
        :param ydata: Array of numbers to be displayed on the Y axis.
        :return: None
        """
        newTab = ttk.Frame(self.tabControl)

        fig = Figure(figsize=(800 / 100, 600 / 100), dpi=100)
        subplot = fig.add_subplot(111)
        if(log==True):
            subplot.semilogy(xdata, ydata)
        elif(log==False):
            subplot.plot(xdata, ydata)

        subplot.set_title(graphTitle)
        subplot.set_ylabel(yLabel)
        subplot.set_xlabel(xLabel)
        #subplot.grid(which='both')
        subplot.grid(which='minor',alpha=0.2)
        subplot.grid(which='major',alpha=0.5)
        subplot.minorticks_on()

        self.tabControl.add(newTab, text=name)

        canvas = FigureCanvasTkAgg(fig, master=newTab)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, newTab)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


    def remove_tab(self, tabNo):
        """
        ramoeve_tab This function removes tab with a given index from the graph window.
        :param tabNo: INdex of the tab to be removed. First tab has index 0.
        :return: None
        """
        tabNum = len(self.tabControl.tabs())
        if tabNo < tabNum:
            self.tabControl.forget(tabNo)
            #print("Invalid tab number to remove!")
    def clear_tabs(self):
        tabNum = len(self.tabControl.tabs())
        if tabNum>0:
            for i in range(0,tabNum):
                self.tabControl.forget(tabNum-1-i)
    



