from tkinter import *
from menu_bar import *

root = Tk()

menu = menu_bar(root=root)
tmp = menu.get_menu_bar()

root.config(menu=tmp)

root.mainloop()
