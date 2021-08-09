# Function to check CSV file isn't empty

from pathlib import Path
from extract_filename import extract_filename

def is_empty(*, file_path):
    """Takes in file path and returns true if it's empty or false if it's not"""
    file_size = Path(file_path).stat().st_size
    filename = extract_filename(file_path=file_path)
    if file_size > 0:
        return False
    else:
        with open("log.txt","at") as log:
            log.write(filename + " is empty\n")
        return True