# Function to check CSV file isn't empty

from pathlib import Path

def is_empty(*, file_path):
    """Takes in file path and returns true if it's empty or false if it's not"""
    file_size = Path(file_path).stat().st_size
    if file_size > 0:
        return False
    else:
        return True