from tkinter import *
from tkinter import ttk
from menu_bar import *

root = Tk()
root.title("ZPB FET")

# Add menu bar to the program window
menu = menu_bar(root=root)
root.config(menu=menu.get_menu_bar())

# Create paned window for display widgets
pw = PanedWindow(orient='horizontal')
# Insert display widgets into paned window
# Graph window

pw.add()

# Parameters display

pw.add()

pw.pack(fill=BOTH, expand=True)
pw.configure(sashrelief=RAISED)



root.mainloop()
