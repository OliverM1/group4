# Creates archive folder in same directory as the Temp folder,
# then archives away validated file in the correct date folder (creating the folder if necessary)

import shutil
from extract_filename import extract_filename
import os


def archive_file(*, file_path):
    filename = extract_filename(file_path=file_path)

    # Extracts date to use in archive file name
    date_and_time = filename.split(".")[0].split("_")[-1]
    year = date_and_time[0:4]
    month = date_and_time[4:6]
    day = date_and_time[6:8]
    archive_name = day + "." + month + "." + year

    # Extracts the file path of the directory containing the temp folder
    main_directory_split = file_path.split("/")
    main_directory_split.pop()
    main_directory_split.pop()
    main_directory = "/".join(main_directory_split)
    archive_directory = main_directory + "/Archive"

    # Checks if Archive file exists and creates it if not
    files_in_main_directory = os.listdir(main_directory)
    if "Archive" not in files_in_main_directory:
        os.mkdir(archive_directory)

    archive_file_path = archive_directory + "/" + archive_name

    # Checks if needed date folder exists in archive folder, and creates it if not
    files_in_archive = os.listdir(archive_directory)
    if archive_name not in files_in_archive:
        os.mkdir(archive_file_path)

    # Moves the file to a folder in the archive corresponding to the file's date
    shutil.move(file_path, archive_file_path + "/" + filename)
