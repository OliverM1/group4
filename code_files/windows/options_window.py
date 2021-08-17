from tkinter import *
from tkinter import ttk, filedialog
import re

from windows.basic_window import BasicWindow
import config

# IP address regex, copied from:
# https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch07s16.html
IP_PATTERN = re.compile((
    "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}"
    "(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
))
# Regex for validating before the complete address has been entered
INCOMPLETE_IP_PATTERN = re.compile("^[0-9.]*$")


class OptionsWindow(BasicWindow):
    """A window for selecting the default directory to save files, and
    configuring the FTP server details."""

    def __init__(self, parent):
        super().__init__(parent, title="Options")

        # Frame for option to set the default directory
        self.frm_directory = ttk.Labelframe(self.frm_contents, text="General")
        self.frm_directory.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

        # Label for the directory entry
        self.lbl_directory = ttk.Label(self.frm_directory,
                                       text="Save files in this directory:")
        self.lbl_directory.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Entry for the directory
        # Can only be changed using the select directory dialog
        self.default_directory = StringVar()
        self.ent_directory = ttk.Entry(self.frm_directory, width=40,
                                       textvariable=self.default_directory,
                                       state="readonly")
        self.ent_directory.grid(row=1, column=0, padx=5, pady=5)

        # Button to open a dialog to choose a directory
        self.btn_browse = ttk.Button(self.frm_directory, text="Browse...",
                                     command=self.get_default_directory)
        self.btn_browse.grid(row=1, column=1, padx=5, pady=5)

        # Frame for options to configure the FTP server details
        self.frm_ftp_setup = ttk.Labelframe(self.frm_contents,
                                            text="FTP configuration")
        self.frm_ftp_setup.grid(row=1, column=0, padx=10, pady=10, sticky=EW)

        # Label for the IP address entry
        self.lbl_ftp_ip = ttk.Label(self.frm_ftp_setup,
                                    text="Server IP address:")
        self.lbl_ftp_ip.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Label for the port entry
        self.lbl_ftp_port = ttk.Label(self.frm_ftp_setup,
                                      text="Port:")
        self.lbl_ftp_port.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Commands for validating the IP and port entries
        self.check_ip_wrapper = (self.register(self.check_ip), "%P", "%V")
        self.check_port_wrapper = (self.register(self.check_port), "%P")

        # Entry for the IP address
        self.ftp_ip = StringVar()
        self.ent_ftp_ip = ttk.Entry(self.frm_ftp_setup, width=16,
                                    textvariable=self.ftp_ip, validate=ALL,
                                    validatecommand=self.check_ip_wrapper)
        self.ent_ftp_ip.grid(row=1, column=0, padx=5, pady=5)

        # Entry for the port
        self.ftp_port = StringVar()
        self.ent_ftp_port = ttk.Entry(self.frm_ftp_setup, width=6,
                                      textvariable=self.ftp_port, validate=ALL,
                                      validatecommand=self.check_port_wrapper)
        self.ent_ftp_port.grid(row=1, column=1, padx=5, pady=5)

        # Configure an extra column to allow the error message to change
        # size without making the IP and port entries move
        self.frm_ftp_setup.columnconfigure(2, weight=1)

        # Error message displayed if the entries are invalid
        self.error_msg = StringVar()
        self.lbl_error = ttk.Label(self.frm_ftp_setup, foreground="red",
                                   textvariable=self.error_msg)
        self.lbl_error.grid(row=2, column=0, columnspan=3, padx=5, pady=5,
                            sticky=W)

        # Variables to track which entries are invalid
        self.invalid_ftp_ip = False
        self.invalid_ftp_port = False

        # Populate the entries with the currently saved options
        self.load_options()

        # Frame for OK and cancel buttons
        self.frm_buttons = ttk.Frame(self.frm_contents)
        self.frm_buttons.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        # Cancel button: close the window without saving anything
        self.btn_cancel = ttk.Button(self.frm_buttons, text="Cancel",
                                     command=self.destroy)
        self.btn_cancel.grid(row=0, column=0, padx=5, pady=5)

        # OK button: save the options and close the window
        self.btn_ok = ttk.Button(self.frm_buttons, text="OK", default=ACTIVE,
                                 command=self.save_options)
        self.btn_ok.grid(row=0, column=1, padx=5, pady=5)

    def get_default_directory(self):
        """Opens a dialog to allow the user to select a default
        directory."""

        dir_name = filedialog.askdirectory()
        if dir_name:
            self.default_directory.set(dir_name)

    def load_options(self):
        """Open the config file and extract the current settings."""

        options = config.load_options()
        self.default_directory.set(options["directory"])
        self.ftp_ip.set(options["ftp_ip"])
        self.ftp_port.set(options["ftp_port"])

    def save_options(self):
        """Save the selected options in the config file and close the
        options window."""

        options = {
            "directory": self.default_directory.get(),
            "ftp_ip": self.ftp_ip.get(),
            "ftp_port": self.ftp_port.get(),
        }
        config.save_options(options)
        self.destroy()

    def update_error_msg(self):
        """Change the error message to tell the user which entries are
        invalid."""

        if self.invalid_ftp_ip and self.invalid_ftp_port:
            message = "Please enter a valid IP address and port"
        elif self.invalid_ftp_ip:
            message = "Please enter a valid IP address"
        elif self.invalid_ftp_port:
            message = "Please enter a valid port"
        else:
            message = ""

        self.error_msg.set(message)

    def update_ok_btn(self):
        """Disable the OK button if there are invalid entries, otherwise
        enable it."""

        if any((self.invalid_ftp_ip, self.invalid_ftp_port)):
            self.btn_ok.state(["disabled"])
        else:
            self.btn_ok.state(["!disabled"])

    def check_ip(self, new_val, op):
        """Validates the FTP IP address entry."""

        # Check if the entry is a valid IP address, and update the error
        # message and OK button state accordingly
        self.invalid_ftp_ip = re.match(IP_PATTERN, new_val) is None
        self.update_error_msg()
        self.update_ok_btn()

        if op == "key":
            # If the user is still typing the address, allow it to be
            # incomplete
            valid_so_far = re.match(INCOMPLETE_IP_PATTERN, new_val) is not None
            return valid_so_far

        return not self.invalid_ftp_ip

    def check_port(self, new_val):
        """Validates the FTP port entry."""

        # Check whether the value is an integer
        try:
            port = int(new_val)
            valid_so_far = True
            # Check whether the port is in the valid range
            self.invalid_ftp_port = not (0 <= port <= 65535)
        except ValueError:
            # Allow the entry to be empty in case the user is still
            # typing
            valid_so_far = new_val == ""
            self.invalid_ftp_port = True

        # Update the error message and OK button state
        self.update_error_msg()
        self.update_ok_btn()

        return valid_so_far


# For testing just this window
# (will not run when the module is imported)
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    window_options = OptionsWindow(root)
    window_options.protocol("WM_DELETE_WINDOW", window_options.master.destroy)
    root.mainloop()
