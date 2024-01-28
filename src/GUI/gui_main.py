from tkinter import *
from tkinter import ttk
from menu_bar import *
from graph_window import *
from parameter_window import *
from transistors import Transistor
import numpy as np
import pandas as pd
from utils import updata_parameter_window, update_graph_window, calc_all_data_for_new_file

root = Tk()
root.title("ZPB FET")
# Create paned window for display widgets
pw = PanedWindow(orient='horizontal')
# Insert display widgets into paned window
# Graph window
graphWindow = graph_window(pw)

pw.add(graphWindow.get_graph_widget())

# Parameters display
parameterWindow = parameter_window(pw,graphWindow)
pw.add(parameterWindow.get_parameter_widget())

# Add menu bar to the program window
menu = Menu_bar(root, parameterWindow, graphWindow)
root.config(menu=menu.get_menu_bar())


pw.pack(fill=BOTH, expand=True)
pw.configure(sashrelief=RAISED)

root.mainloop()
