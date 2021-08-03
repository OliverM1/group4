# Checking file name to see whether the file has already been stored (Assumes filename already checked)

import pickle

def is_duplicate_file(*, filepath):
    """Loads list of names of already downloaded files as array straight from pickle file, then checks the current filename against the list.
    if filename is not duplicate it adds the name to the list"""
    # Note: filepath string must have format ../../../../../.. ( "/" not "\" )

    # Loads list from pickle file
    pickle_file = open("filename_list_pickle", "rb")
    name_list = pickle.load(pickle_file)
    pickle_file.close()

    # Returns true if name is duplicate or false otherwise
    filename = filepath.split("/")[-1]
    if filename in name_list:
        return True
    else:
        # Adds the new name to the pickle list
        name_list.append(filename)
        pickle_file = open("filename_list_pickle", "wb")
        pickle.dump(name_list, pickle_file)
        pickle_file.close()
        return False
