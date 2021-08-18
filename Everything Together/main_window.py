from tkinter import *
from tkinter import ttk, font, messagebox
from PIL import Image, ImageTk

from basic_window import BasicWindow
from options_window import OptionsWindow
from download_window import DownloadWindow
from date_select_window import DateSelectWindow

from ftp_client import ftpclient
from config import load_options
from regex import today_date,make_regex
from ftp_client import ftpclient
from check_runner import run_checks
from cleanup import cleanup

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
            command=self.open_download_window_today
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
        window_options.lift()  # Show above main window
        # TODO: block the user from interacting with the main window
        #   while the options window is open
        window_options.focus_force()

    def open_download_window(self):  # TODO
        window_download = DownloadWindow(self.master)
        window_download.lift()  # Show above main window
        window_download.focus_force()

    def open_download_window_today(self):
        options = load_options()
        ip = options.get("ftp_ip")
        port = int(options.get("ftp_port"))
        today = today_date()
        regexstr = make_regex(today)

        ftp = ftpclient(server_ip=ip,port=port,regex_str=regexstr)
        ftp.connect()
        files = ftp.match()
        #store value and pass across connect - Uncomment as well as the download window at some point
        #with open("files_number","w+")as f:
        #    f.write(files)
        #    f.close()

        #Write somewhere else
        ftp.download()

        # window_download = DownloadWindow(self.master)
        # window_download.lift()  # Show above main window
        # window_download.focus_force()

        run_checks()
        cleanup()

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
        Image.open("images/survey-2316468_1280.png").resize((200, 200))
    )
    window_main = MainWindow(root, img_icon)
    root.mainloop()
