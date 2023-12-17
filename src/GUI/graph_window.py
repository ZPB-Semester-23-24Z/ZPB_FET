from tkinter import *
from tkinter import ttk


class graph_window:

    def __init__(self, root):
        self.root = root
        # Create empty tab. Tabs with graphs will be created after file is opened.
        self.tabControl = ttk.Notebook(root)
        emptyTab = ttk.Frame(self.tabControl)
        self.tabControl.add(emptyTab, text="Tab 1")
        self.tabControl.pack(expand=1, fill="both")
        ttk.Label(emptyTab, text="Open data file").pack(expand=True)

    def get_graph_widget(self) -> ttk.Notebook:
        return self.tabControl

    def add_tab(self, name: str, text: str):
        newTab = ttk.Frame(self.tabControl)
        self.tabControl.add(newTab, text=name)
        ttk.Label(newTab, text=text).pack(expand=True)

    def remove_tab(self, tabNo):
        self.tabControl.forget(tabNo)

    def get_tab_number(self) -> int:
        tabList = self.tabControl.tabs
        return tabList.len()
