# Checking file name to see whether the file has already been stored (Assumes filename already checked)

import pickle
from extract_filename import extract_filename


def is_duplicate_file(*, file_path):
    """Loads list of names of already downloaded files as array straight from pickle file, then checks the current filename against the list.
    if filename is not duplicate it adds the name to the list"""
    # Note: filepath string must have format ../../../../../.. ( "/" not "\" )

    # Loads list from pickle file
    pickle_file = open("filename_list_pickle", "rb")
    name_list = pickle.load(pickle_file)
    pickle_file.close()

    # Returns true if name is duplicate or false otherwise
    filename = extract_filename(file_path=file_path)
    if filename in name_list:
        with open("log.txt", "at") as log:
            log.write(filename + " is a duplicate\n")
        return True
    else:
        return False