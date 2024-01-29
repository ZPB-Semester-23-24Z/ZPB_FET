from tkinter import *
from menu_bar import *
from graph_window import *
from parameter_window import *

root = Tk()
root.title("ZPB FET")

menu = Menu_bar(root)
root.config(menu=menu.get_menu_bar())

root.mainloop()
