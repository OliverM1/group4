from tkinter import *
from tkinter import ttk, font
from PIL import Image, ImageTk

from windows.basic_window import BasicWindow
from windows.options_window import OptionsWindow
from windows.download_window import DownloadWindow
from windows.date_select_window import DateSelectWindow


class MainWindow(BasicWindow):
    """The window that is displayed when the application is opened,
    containing buttons to access various functions."""

    def __init__(self, parent, icon):
        super().__init__(parent, title="Download Medical Data")

        # Closing the main window should close the application, so it
        # must destroy the (hidden) root window
        self.protocol("WM_DELETE_WINDOW", parent.destroy)

        # Label with a logo and title
        title_font = font.Font(family="TkDefaultFont", size=30, weight="bold")
        self.lbl_title = ttk.Label(self.frm_contents, font=title_font,
                                   text="Venus Medical\nResearch",
                                   justify=CENTER, anchor=CENTER,
                                   image=icon, compound="top")
        self.lbl_title.grid(row=0, column=0, padx=100, pady=20)

        # Frame for buttons
        self.frm_buttons = ttk.Frame(self.frm_contents)
        self.frm_buttons.grid(row=1, column=0, pady=5)

        # Buttons to download today's files, open a date selection
        # window, and open an options window
        self.btn_download_today = ttk.Button(
            self.frm_buttons, text="Download Today's Data", default=ACTIVE,
            command=self.open_download_window
        )
        self.btn_select_dates = ttk.Button(
            self.frm_buttons, text="Select Dates to Download...",
            command=self.open_date_select_window
        )
        self.btn_options = ttk.Button(
            self.frm_buttons, text="Options...",
            command=self.open_options_window
        )

        # Place the buttons on the screen
        buttons = [self.btn_download_today, self.btn_select_dates,
                   self.btn_options]
        for idx, btn in enumerate(buttons):
            btn.grid(row=idx, column=0, sticky=EW, pady=5)

    def open_options_window(self):
        """Opens the options window which takes focus from the main
        window."""

        window_options = OptionsWindow(self.master)
        window_options.lift()
        window_options.grab_set()

    def open_download_window(self):
        """Opens the download window which takes focus from the main
        window."""

        window_download = DownloadWindow(self.master)
        window_download.lift()
        window_download.grab_set()

    def open_date_select_window(self):
        """Opens the date selection window which takes focus from the
        main window."""

        window_date_select = DateSelectWindow(self.master)
        window_date_select.lift()
        window_date_select.grab_set()


# For testing just this window
# (will not run when the module is imported)
if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    img_icon = ImageTk.PhotoImage(
        Image.open("../images/survey-2316468_1280.png").resize((200, 200))
    )
    window_main = MainWindow(root, img_icon)
    root.mainloop()
