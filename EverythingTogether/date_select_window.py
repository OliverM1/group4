from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

from basic_window import BasicWindow
from download_window import DownloadWindow
from config import load_options
from regex import make_regex
from cleanup import cleanup
from ftp_client import ftpclient
from check_runner import run_checks

class DateSelectWindow(BasicWindow):
    """A window to select a date to download files from."""

    def __init__(self, parent):
        super().__init__(parent, title="Select Date")

        # Frame for date selection
        self.frm_dates = ttk.Frame(self.frm_contents)
        self.frm_dates.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

        # Label for date
        self.lbl_date = ttk.Label(self.frm_dates, text="Download files from:")
        self.lbl_date.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Entry for date
        # Can only be changed using the calendar drop down
        self.selected_date = StringVar()
        self.ent_date = DateEntry(self.frm_dates, state="readonly",
                                  date_pattern="yyyy-mm-dd",
                                  textvariable=self.selected_date)
        self.ent_date.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        # Frame for OK and cancel buttons
        self.frm_buttons = ttk.Frame(self.frm_contents)
        self.frm_buttons.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        # Cancel button: close the window without doing anything
        self.btn_cancel = ttk.Button(self.frm_buttons, text="Cancel",
                                     command=self.destroy)
        self.btn_cancel.grid(row=0, column=0, padx=5, pady=5)

        # OK button: proceed to downloading from the selected date
        self.btn_ok = ttk.Button(self.frm_buttons, text="OK", default=ACTIVE,
                                 command=self.open_download_window)
        self.btn_ok.grid(row=0, column=1, padx=5, pady=5)

    def open_download_window(self):
        """Attempt to download the files from the selected date."""
        date = str(self.ent_date_start.get_date()).split("-")
        datestr = ""
        for item in date:
            datestr = datestr + item

        options = load_options()
        ip = options.get("ftp_ip")
        port = int(options.get("ftp_port"))
        regexstr = make_regex(datestr)

        ftp = ftpclient(server_ip=ip,port=port,regex_str=regexstr)
        ftp.connect()
        files = ftp.match()

        #store value and pass across connect - Uncomment as well as the download window at some point
        #with open("files_number","w+")as f:
        #    f.write(files)
        #    f.close()

        ftp.download()

        #window_download = DownloadWindow(self.master)
        #window_download.grab_set()

        run_checks()
        cleanup()

        self.destroy()

# For testing just this window
# (will not run when the module is imported)
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    window_date_select = DateSelectWindow(root)
    window_date_select.protocol("WM_DELETE_WINDOW",
                                window_date_select.master.destroy)
    root.mainloop()
