# Check to see if any of the columns of a row in a file are empty
# Will write to the log if this is the case
from csv_reader import fileToCSV
import os


def ColCheck(*, file_path):
    csv_file = fileToCSV(file_path=file_path)
    filename = os.path.basename(file_path)
    for row in csv_file:
        for item in row:
            if row[item]=="":
                with open("log.txt", "at") as log:
                    log.write(filename + " has missing columns\n")
                return True
    return False



