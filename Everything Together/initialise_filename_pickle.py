# Creates initial pickle file of just an empty list

import pickle
def make_pickle_file():
    pickle_file = open("filename_list_pickle", "wb")
    pickle.dump([], pickle_file)
    pickle_file.close()