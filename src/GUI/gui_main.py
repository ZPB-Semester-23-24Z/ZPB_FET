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

menu = Menu_bar(root)
root.config(menu=menu.get_menu_bar())

root.mainloop()
