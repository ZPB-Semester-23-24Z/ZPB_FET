from tkinter import *


class menu_bar:

    def __init__(self, root):
        self.menubar = Menu(root)
        self.root = root

        #create file menu
        filemenu = self.setup_file_menu()
        self.menubar.add_cascade(label="File", menu=filemenu)

        #create edit menu
        helpmenu = self.setup_help_menu()
        self.menubar.add_cascade(label="Help", menu=helpmenu)

    #file menu handlers
    def filemenu_new(self):
        #TDOD: add new file handling
        pass

    def filemenu_open(self):
        # TDOD: add opne file handling
        pass

    def filemenu_save(self):
        # TDOD: add save file handling
        pass

    #Help menu handlers
    def helpmenu_about(self):
        # TDOD: add about information
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

