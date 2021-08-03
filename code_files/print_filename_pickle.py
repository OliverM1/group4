# Prints contents of filename_list_pickle

import pickle

pickle_file = open("filename_list_pickle", "rb")
name_list = pickle.load(pickle_file)
pickle_file.close()
print(name_list)