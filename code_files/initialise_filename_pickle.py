# Creates initial pickle file of just an empty list

import pickle

pickle_file = open("filename_list_pickle", "wb")
pickle.dump([], pickle_file)
pickle_file.close()