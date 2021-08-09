
# Checks to see if there are duplicated batch ids in the dictionary of the file
# Will write to log if this is the case

from csv_reader import fileToCSV
from extract_filename import extract_filename as extract


def batchIDCheck(*, file_path):
    csvFile = fileToCSV(file_path=file_path)
    filename = extract(file_path=file_path)
    ids = []
    for row in csvFile:
        ids.append(row["batch_id"])
    removed = dict.fromkeys(ids)
    if len(removed) != len(ids):
        with open("log.txt", "at") as log:
            log.write(filename + " has duplicate batch ids\n")
        return True
    else:
        return False
