from tkinter import *
from PIL import Image, ImageTk

from windows.main_window import MainWindow

# Initialise Tk.  We don't need the root window, so don't display it.
root = Tk()
root.withdraw()

# I wanted to put this in the MainWindow class but the image didn't
# display.  It also didn't raise any exceptions, so I have literally no
# clue why it didn't work.
img_icon = ImageTk.PhotoImage(
    Image.open("images/survey-2316468_1280.png").resize((200, 200))
)

# Create the main window and start the event loop
window_main = MainWindow(root, img_icon)
root.mainloop()
