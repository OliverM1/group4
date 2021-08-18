from tkinter import *
from tkinter import ttk


class BasicWindow(Toplevel):
    """A window template that all other windows are derived from."""

    def __init__(self, parent=None, title="", **kwargs):
        super().__init__(parent, **kwargs)

        # Set up the window
        self.title(title)
        self.resizable(FALSE, FALSE)

        # Frame to hold all widgets
        self.frm_contents = ttk.Frame(self)
        self.frm_contents.grid(row=0, column=0, sticky=NSEW)
