import datetime
import re

FILENAME_PATTERN = re.compile("^MED_DATA_[0-9]{14}\\.csv$")
DATE_PATTERN = re.compile("[0-9]{14}")
DATE_FORMAT = [4, 2, 2, 2, 2, 2]  # YYYYMMDDHHMMSS
MIN_DATE = datetime.datetime(1970, 1, 1)  # date of earliest valid file


# This will get the filename, which will then be checked by
# is_valid_filename()
def get_filename():
    pass


def is_valid_filename(filename: str) -> bool:
    """Checks the filename of a data file.

    Filenames should use the following naming convention:
    MED_DATA_YYYYMMDDHHMMSS.csv

    Returns True if the filename is valid, False otherwise."""

    is_valid = True
    current_date = datetime.datetime.now()

    if not FILENAME_PATTERN.match(filename):
        is_valid = False

    else:
        # Extract timestamp portion of filename
        timestamp = DATE_PATTERN.search(filename)[0]

        # Split timestamp into year, month, day, hour, minute, second
        it = iter(timestamp)
        year, month, day, hour, minute, second = [
            int("".join([next(it) for i in range(size)]))
            for size in DATE_FORMAT
        ]

        try:
            # If this fails, the timestamp is not a valid date
            # (e.g. month 13)
            file_date = datetime.datetime(
                year, month, day, hour, minute, second
            )

            # Reject files with dates in the future or from before the
            # first data were collected
            if not (MIN_DATE <= file_date <= current_date):
                is_valid = False

        except ValueError:
            is_valid = False

    return is_valid


# For testing
if __name__ == "__main__":
    while True:
        name = input("Enter filename to check: ")
        print(is_valid_filename(name))
