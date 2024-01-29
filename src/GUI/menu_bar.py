from tkinter import *
from graph_window import *
from parameter_window import *
from compare_window import *
from tkinter import filedialog
from utils import updata_parameter_window, update_graph_window, calc_all_data_for_new_file, update_model
from transistors import Transistor
import os

class Menu_bar:
    Transistors = []
    compare_window_active = False
    preview_window_active = False

    def __init__(self, root):
        self.menubar = Menu(root)
        self.root = root
        #self.parameterWindow = parameterWindow
        #self.graphWindow = graphWindow
        self.pw = None

        # create file menu
        filemenu = self.setup_file_menu()
        self.menubar.add_cascade(label="File", menu=filemenu)

        # create edit menu
        helpmenu = self.setup_help_menu()
        self.menubar.add_cascade(label="Help", menu=helpmenu)

        # create compare menu
        self.comparemenu = self.setup_compare_window()
        self.menubar.add_cascade(label="Working Mode", menu=self.comparemenu)

        self.preview_window()

    def filemenu_new(self):
        # TODO: add new file handling
        pass

    def filemenu_open(self):
        filePath = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title="Select a File",
                                              filetypes=(("Excel files", "*.xlsx*"),
                                                         ("Text files", "*.csv*"),
                                                         ("all files", "*.*")))

        print("File Opened: " + filePath)
        t = calc_all_data_for_new_file(filePath)
        self.Transistors.append(t)
        print(self.Transistors[-1].name)
        self.parameterWindow.Transistors = self.Transistors
        update_model(self.parameterWindow, t)
        updata_parameter_window(self.parameterWindow, t)
        update_graph_window(self.graphWindow, t)
        if self.compare_window_active:
            self.compare_window()

    def compare_window(self):
        self.compare_window_active = True
        self.preview_window_active = False
        if self.pw is not None:
            self.pw.destroy()

        self.pw = PanedWindow(self.root, orient='horizontal')
        graphWindow = CompareCharsWindow(self.pw)
        self.pw.add(graphWindow.get_graph_widget())

        parameterWindow = CompareWindow(self.pw, self.Transistors, graphWindow)
        self.parameterWindow.Transistors = self.Transistors
        self.pw.add(parameterWindow.get_parameter_widget())

        self.pw.pack(fill=BOTH, expand=True)
        self.pw.configure(sashrelief=RAISED)

        self.parameterWindow = parameterWindow
        self.parameterWindow.Transistors = self.Transistors
        self.graphWindow = graphWindow

    def preview_window(self):
        self.compare_window_active = False
        self.preview_window_active = True
        if self.pw is not None:
            self.pw.destroy()

        self.pw = PanedWindow(self.root, orient='horizontal')
        graphWindow = graph_window(self.pw)

        self.pw.add(graphWindow.get_graph_widget())

        parameterWindow = parameter_window(self.pw, graphWindow, self.Transistors)
        self.pw.add(parameterWindow.get_parameter_widget())

        self.pw.pack(fill=BOTH, expand=True)
        self.pw.configure(sashrelief=RAISED)

        self.parameterWindow = parameterWindow
        self.parameterWindow.Transistors = self.Transistors
        self.graphWindow = graphWindow
        self.parameterWindow.Transistors = self.Transistors
        if len(self.Transistors) > 0:
            update_model(self.parameterWindow, self.Transistors[-1])
            updata_parameter_window(self.parameterWindow, self.Transistors[-1])
            update_graph_window(self.graphWindow, self.Transistors[-1])

    def setup_compare_window(self) -> Menu:
        comparemenu = Menu(self.menubar, tearoff=0)
        comparemenu.add_command(label="Compare Files", command=self.compare_window)
        comparemenu.add_command(label="Preview Files", command=self.preview_window)
        return comparemenu

    def filemenu_save(self):
        # TODO: add save file handling
        pass

    def filemenu_save_as(self):
        # TODO: add save as file handling
        pass

    def helpmenu_about(self):
        # TODO: add about information
        pass

    def get_menu_bar(self) -> Menu:
        return self.menubar

    def setup_file_menu(self) -> Menu:
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.filemenu_new)
        filemenu.add_command(label="Open", command=self.filemenu_open)
        filemenu.add_command(label="Save", command=self.filemenu_save)
        filemenu.add_command(label="Save as", command=self.filemenu_save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        return filemenu

    def setup_help_menu(self) -> Menu:
        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="About...", command=self.helpmenu_about)
        return helpmenu
