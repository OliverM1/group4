from tkinter import *
from tkinter import ttk

from basic_window import BasicWindow
import os

class DownloadWindow(BasicWindow):
    """A window to show download progress."""

    def __init__(self, parent):
        super().__init__(parent, title="Downloading Files")

        if (os.path.isfile("files_number")):
            with open("files_number","r") as f:
                self.num_files = int(f.read())
                f.close()
        else:       
                #use some default
                self.num_files = 10


        # Frame for progress bar
        self.frm_progress = ttk.Frame(self.frm_contents)
        self.frm_progress.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

        # Label for the progress bar
        self.progress_text = StringVar()
        self.lbl_progress = ttk.Label(self.frm_progress,
                                      textvariable=self.progress_text)
        self.lbl_progress.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Progress bar for the download
        self.progress_value = IntVar(value=0)
        self.progress_bar = ttk.Progressbar(
            self.frm_progress, orient=HORIZONTAL, mode="determinate",
            maximum=self.num_files, variable=self.progress_value, length=300
        )
        self.progress_bar.grid(row=1, column=0, padx=5, pady=5, sticky=EW)

        # Frame for buttons
        self.frm_buttons = ttk.Frame(self.frm_contents)
        self.frm_buttons.grid(row=1, column=0, padx=10, pady=10, sticky=EW)
        self.frm_buttons.columnconfigure(0, weight=1)

        # Close button
        self.btn_close = ttk.Button(self.frm_buttons, text="Close",
                                    command=self.destroy)
        self.btn_close.grid(row=0, column=0, padx=5, pady=5)

        self.update_progress()

    # TODO: rewrite the update_progress method when downloading files is
    #  implemented
    def update_progress(self, num_downloaded=0):
        """Update the progress bar and label as files are downloaded."""

        if num_downloaded < self.num_files:
            self.progress_value.set(num_downloaded)
            self.progress_text.set(
                f"Downloading file {num_downloaded+1} of {self.num_files}..."
            )
            self.btn_close.state(["disabled"])
            self.after(1000, self.update_progress, num_downloaded + 1)
        else:
            self.progress_value.set(self.num_files)
            self.progress_text.set(f"Downloaded {self.num_files} files.")
            self.btn_close.state(["!disabled"])


# For testing just this window
# (will not run when the module is imported)
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    window_download = DownloadWindow(root)
    window_download.protocol("WM_DELETE_WINDOW", window_download.master.destroy)
    root.mainloop()
