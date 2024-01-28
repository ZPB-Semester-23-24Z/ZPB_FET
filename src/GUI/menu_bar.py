from tkinter import *
from graph_window import *
from parameter_window import *
from tkinter import filedialog
from utils import updata_parameter_window, update_graph_window, calc_all_data_for_new_file, update_model
from transistors import Transistor
from compare_window import *
from compare_window import CompareCharsWindow
from compare_window import CompareWindow
import os
class Menu_bar:
    Transistors=[]
    def __init__(self, root):
        self.menubar = Menu(root)
        self.root = root
        self.pw=0
        # create file menu
        filemenu = self.setup_file_menu()
        self.menubar.add_cascade(label="File", menu=filemenu)
        modemenu = self.setup_mode_menu()
        self.menubar.add_cascade(label="Mode", menu=modemenu)

        # create edit menu
        helpmenu = self.setup_help_menu()
        self.menubar.add_cascade(label="Help", menu=helpmenu)

    # file menu handlers
    def filemenu_new(self):
        # TODO: add new file handling
        pass
    def mode_menu_single(self):
        self.single_mode()
        pass
    def mode_menu_compare(self):
        self.compare_mode()
        pass
    def filemenu_open(self):
        # TODO: might want to change initial directory path and file types
        filePath = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title="Select a File",
                                              filetypes=(("Excel files",
                                                          "*.xlsx*"),
                                                         ("Text files",
                                                          "*.csv*"),
                                                         ("all files",
                                                          "*.*")))

        # TODO: do something with extracted file path
        print("File Opened: " + filePath)
        t = calc_all_data_for_new_file(filePath)
        self.Transistors.append(t)
        print(self.Transistors[-1].name)
        self.parameterWindow.Transistors=self.Transistors
        update_model(self.parameterWindow, t)
        updata_parameter_window(self.parameterWindow, t)
        update_graph_window(self.graphWindow, t)

        pass

    def filemenu_save(self):
        # TODO: add save file handling
        pass

    def filemenu_save_as(self):
        # TODO: add save as file handling
        pass

    #Help menu handlers
    def helpmenu_about(self):
        # TODO: add about information
        pass



    def get_menu_bar(self) -> Menu:
        """
        get_menu_bar returns created menu bar object
        :return: menubar widget created in this class
        """
        return self.menubar

    def setup_file_menu(self) -> Menu:
        """
        setup_file_menu creates File menu and connects handlers to their respective commands.
        :return: filemeniu object
        """
        filemenu = Menu(self.menubar, tearoff=0) #tearoff=0 - menu cannot be deteched from the menu bar
        filemenu.add_command(label="New", command=self.filemenu_new)
        filemenu.add_command(label="Open", command=self.filemenu_open)
        filemenu.add_command(label="Save", command=self.filemenu_save)
        filemenu.add_command(label="Save as", command=self.filemenu_save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        return filemenu

    def setup_help_menu(self) -> Menu:
        """
        setup_help_menu creates Help menu and connects handlers to their respective commands.
        :return: filemeniu object
        """
        helpmenu = Menu(self.menubar, tearoff=0) #tearoff=0 - menu cannot be deteched from the menu bar
        helpmenu.add_command(label="About...", command=self.helpmenu_about)
        return helpmenu

    def setup_mode_menu(self) -> Menu:
        """
        setup_help_menu creates Help menu and connects handlers to their respective commands.
        :return: filemeniu object
        """
        helpmenu = Menu(self.menubar, tearoff=0) #tearoff=0 - menu cannot be deteched from the menu bar
        helpmenu.add_command(label="Compare", command=self.mode_menu_compare)
        helpmenu.add_command(label="Single", command=self.mode_menu_single)
        return helpmenu
    def single_mode(self):
        if(self.pw!=0):
            self.pw.destroy()
        self.pw=PanedWindow(orient='horizontal')
        self.graphWindow = graph_window(self.pw)
        self.pw.add(self.graphWindow.get_graph_widget())
        self.parameterWindow=parameter_window(self.pw,self.graphWindow)
        self.pw.add(self.parameterWindow.get_parameter_widget())
        self.pw.pack(fill=BOTH, expand=True)
        self.pw.configure(sashrelief=RAISED)
    def compare_mode(self):
        if(self.pw!=0):
            self.pw.destroy()
        t_array = []
        t_array.append(calc_all_data_for_new_file("res/FET1.xlsx"))
        t_array.append(calc_all_data_for_new_file("res/FETs_1.xlsx"))
        t_array.append(calc_all_data_for_new_file("res/FETs_2.xlsx"))
        t_array.append(calc_all_data_for_new_file("res/FETs.xlsx"))
        self.pw=PanedWindow(orient='horizontal')
        self.graphWindow = CompareCharsWindow(self.pw)
        self.pw.add(self.graphWindow.get_graph_widget())
        self.parameterWindow = CompareWindow(self.pw, t_array, self.graphWindow)
        self.pw.add(self.parameterWindow.get_parameter_widget())
        self.pw.pack(fill=BOTH, expand=True)
        self.pw.configure(sashrelief=RAISED)
