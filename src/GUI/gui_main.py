from tkinter import *
from tkinter import ttk
from menu_bar import *
from graph_window import *

root = Tk()
root.title("ZPB FET")

# Add menu bar to the program window
menu = menu_bar(root)
root.config(menu=menu.get_menu_bar())

# Create paned window for display widgets
pw = PanedWindow(orient='horizontal')
# Insert display widgets into paned window
# Graph window
graphWindow = graph_window(pw)
pw.add(graphWindow.get_graph_widget())

# Parameters display
bot = Checkbutton(pw, text ="Choose Me !")
bot.pack(side=TOP)
pw.add(bot)

pw.pack(fill=BOTH, expand=True)
pw.configure(sashrelief=RAISED)

root.mainloop()
