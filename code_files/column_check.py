# Check to see if any of the columns of a row in a file are empty
# Will write to the log if this is the case
from csv_reader import fileToCSV
from extract_filename import extract_filename as extract


def ColCheck(*, file_path):
    csv_file = fileToCSV(file_path=file_path)
    filename = extract(file_path=file_path)
    # Nesting could be made more efficient in the future
    for row in csv_file:
        for item in row:
            if row[item]=="":
                with open("log.txt", "at") as log:
                    log.write(filename + " has missing columns\n")
                return True
    return False



