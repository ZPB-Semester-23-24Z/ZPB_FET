from tkinter import *
from tkinter import ttk
from menu_bar import *
from graph_window import *
import numpy as np

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

# Setup dummy data
xdata = np.arange(0, 3, .01)
ydata = 2 * np.sin(2 * np.pi * xdata)
VD = np.arange(0, 3, .01)
ID = 0.00000000000000000000000001*(np.exp(VD/(2*0.025))-1)

graphWindow.add_tab("Graph 1", "Graph 1", "X", "Y", xdata, ydata)
graphWindow.add_tab("Graph 2", "Graph 2", "X", "Y", VD, ID)
graphWindow.remove_tab(0)


root.mainloop()
