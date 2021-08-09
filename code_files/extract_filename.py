# Takes filepath and extracts filename

def extract_filename(*, file_path):
    filepath_split = file_path.split("/")
    return filepath_split[-1]

