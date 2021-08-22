import os

from column_check import ColCheck
from data_in_range_check import datachecker
from filename_check import is_valid_filename
from is_duplicate_file_check import is_duplicate_file
from is_empty_file_check import is_empty
from batchid_check import batchIDCheck
from column_headers_check import column_header_check

from archive_checked_file import archive_file

def run_checks():

    temp = os.path.join(os.getcwd(),"temp")
    files = os.listdir(temp)

    for file in files:
        path = os.path.join(temp,file)
        col = ColCheck(file_path=path)
        data = datachecker(file_path=path)
        name = is_valid_filename(file_path=path)
        duplicate = is_duplicate_file(file_path=path)
        empty = is_empty(file_path=path)
        id = batchIDCheck(file_path=path)
        header = column_header_check(file_path=path)

        if col or data or name or duplicate or empty or id or header:
            pass
        else:
            
            archive_file(file_path=path)