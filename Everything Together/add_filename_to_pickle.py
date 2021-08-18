# Adds the new file name to the pickle list after it's been checked

from extract_filename import extract_filename
import pickle


def add_filename_to_list(*, file_path):

    pickle_file = open("filename_list_pickle", "rb")
    name_list = pickle.load(pickle_file)
    pickle_file.close()

    pickle_file = open("filename_list_pickle", "wb")
    file_name = extract_filename(file_path=file_path)
    name_list.append(file_name)
    pickle.dump(name_list, pickle_file)
    pickle_file.close()