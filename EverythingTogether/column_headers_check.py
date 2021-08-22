# Checks column headers against given list and gives error message if format incorrect

import csv
import os

# Need to edit to fit in with other functions (and needs to be turned into a function)
def column_header_check(*, file_path):
    filename = os.path.basename(file_path=file_path)
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        column_names = []
        for row in csv_reader:
            column_names.append(row)
            break

    if column_names != [["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6", "reading7", "reading8", "reading9", "reading10"]]:
        with open("log.txt", "at") as log:
            log.write(filename + " has a missing column\n")
        return True
    else:
        return False
