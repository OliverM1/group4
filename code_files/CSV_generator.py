# Function to generate CSV files with specific faults for testing data verification

import csv
import random as ran
import date_format as df


def create_batch_ids():
    batch_ids = []
    while len(batch_ids)<10:
        batchid = ran.randint(1, 199)
        if batchid not in batch_ids:
            batch_ids.append(batchid)
    return batch_ids


def empty_csv(year, month, day, start, num):
    """Creates 'num' amount of empty csv files"""
    for i in range(start, start + num):
        with open("MED_DATA_" + df.year_format(year,month,day) + df.time_format(i) + ".csv", "w", newline="") as csvfile:
            mywriter = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)


def correct_csv(year, month, day, start, num):
    """Creates 'num' amount of correctly formatted csv files"""
    for i in range(start, start + num):
        with open("MED_DATA_" + df.year_format(year,month,day) + df.time_format(i) + ".csv", "w", newline="") as csvfile:
            mywriter = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

            mywriter.writerow(["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6", "reading7", "reading8", "reading9", "reading10"])
            batch_ids = create_batch_ids()
            for n in range(0, 10):
                row = [batch_ids[n], "00:00:00"]
                for m in range(0, 10):
                    row.append(round(ran.random()*10, 3))
                mywriter.writerow(row)


def misspelled_header_csv(year, month, day, start, num):
    """Creates 'num' amount of csv files with a misspelled header"""
    misspelled = ["batch", "time", "read", "read", "read", "read", "read", "read", "read", "read", "read", "read"]
    for i in range(start, start + num):
        with open("MED_DATA_" + df.year_format(year,month,day) + df.time_format(i) + ".csv", "w", newline="") as csvfile:
            mywriter = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

            header = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6",
                 "reading7", "reading8", "reading9", "reading10"]
            error_id = ran.randint(0, 11)
            header[error_id] = misspelled[error_id]

            mywriter.writerow(header)
            batch_ids = create_batch_ids()
            for n in range(0, 10):
                row = [batch_ids[n], "00:00:00"]
                for m in range(0, 10):
                    row.append(round(ran.random() * 10, 3))
                mywriter.writerow(row)

def missing_header_csv(year, month, day, start, num):
    """Creates 'num' amount of csv files with a missing header"""

    for i in range(start, start + num):
        with open("MED_DATA_" + df.year_format(year,month,day) + df.time_format(i) + ".csv", "w", newline="") as csvfile:
            mywriter = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

            header = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6",
                 "reading7", "reading8", "reading9", "reading10"]
            error_id = ran.randint(0, 11)
            del header[error_id]

            mywriter.writerow(header)
            batch_ids = create_batch_ids()
            for n in range(0, 10):
                row = [batch_ids[n], "00:00:00"]
                for m in range(0, 10):
                    row.append(round(ran.random() * 10, 3))
                mywriter.writerow(row)


def missing_column_csv(year, month, day, start, num):
    """Creates 'num' amount of csv files with a missing column"""

    for i in range(start, start + num):
        with open("MED_DATA_" + df.year_format(year,month,day) + df.time_format(i) + ".csv", "w", newline="") as csvfile:
            mywriter = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

            header = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6",
                 "reading7", "reading8", "reading9", "reading10"]
            error_id = ran.randint(0, 11)
            del header[error_id]

            mywriter.writerow(header)
            batch_ids = create_batch_ids()
            for n in range(0, 10):
                row = [batch_ids[n], "00:00:00"]
                for m in range(0, 10):
                    row.append(round(ran.random() * 10, 3))

                del row[error_id]
                mywriter.writerow(row)


def invalid_entry_csv(year, month, day, start, num):
    """Creates 'num' amount of csv files with an invalid entry, never the batchid"""

    for i in range(start, num + start):
        with open("MED_DATA_" + df.year_format(year,month,day) + df.time_format(i) + ".csv", "w", newline="") as csvfile:
            mywriter = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

            header = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6",
                 "reading7", "reading8", "reading9", "reading10"]
            mywriter.writerow(header)

            error_row = ran.randint(1, 10)
            error_column = ran.randint(1, 11)

            batch_ids = create_batch_ids()
            for n in range(0, 10):
                if error_column == 1:
                    row = [batch_ids[n], "00:00:70"]
                else:
                    row = [batch_ids[n], "00:00:00"]
                    for m in range(0, 10):
                        row.append(round(ran.random() * 10, 3))
                    if n == error_column - 2:
                        row[error_column] += 10

                mywriter.writerow(row)


def duplicate_batch_id_csv(year, month, day, start, num):
    """Creates 'num' amount of csv files with a duplicate batch_id"""

    for i in range(start, start + num):
        with open("MED_DATA_" + df.year_format(year,month,day) + df.time_format(i) + ".csv", "w", newline="") as csvfile:
            mywriter = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

            header = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6",
                 "reading7", "reading8", "reading9", "reading10"]
            choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            duplicate_id1 = ran.randint(1, 10)
            choices.remove(duplicate_id1)
            duplicate_index = ran.randint(0, 8)
            duplicate_id2 = choices[duplicate_index]
            dup1 = min(duplicate_id1, duplicate_id2)
            dup2 = max(duplicate_id1, duplicate_id2)

            mywriter.writerow(header)
            for n in range(0, 10):
                row = [ran.randint(1, 199), "00:00:00"]
                if n == dup1:
                    dup_id = row[0]
                elif n == dup2:
                    row[0] = dup_id

                for m in range(0, 10):
                    row.append(round(ran.random() * 10, 3))

                mywriter.writerow(row)


def incorrect_filename_csv(year, month, day, start, num):
    """Creates 'num' amount of csv files with an incorrect filename,
    currently it's set to be correct except for reading MED_DATB instead of MED_DATA"""

    for i in range(start, start + num):
        with open("MED_DATB_" + df.year_format(year,month,day) + df.time_format(i) + ".csv", "w", newline="") as csvfile:
            mywriter = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

            header = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6",
                 "reading7", "reading8", "reading9", "reading10"]

            mywriter.writerow(header)
            batch_ids = create_batch_ids()
            for n in range(0, 10):
                row = [batch_ids[n], "00:00:00"]
                for m in range(0, 10):
                    row.append(round(ran.random() * 10, 3))

                mywriter.writerow(row)


def csv_generator(*, year="2021", month="1", day="1", empty=0, correct=0, missing_header=0,
                  missing_column=0, invalid_entries=0, duplicate_batch_ids=0, incorrect_filename=0):
    """"Takes the date and the number of each type of file you'd like to generate and creates them,
    naming starts at MED_DATA_YYYYMMDD000000.csv and goes up in seconds
    (where YYYYMMDD corresponds to the date you entered)."""

    # This limits the number of files that can be created at once adn returns an
    # error message if the user asks for too many
    MAX_LIMIT = 100
    max = empty + correct + missing_header + missing_column + invalid_entries + duplicate_batch_ids + incorrect_filename
    if max > MAX_LIMIT:
        print("Too many files requested! Maximum is", MAX_LIMIT)
        return 1

    # Each type of file is generated in order, then the total is added to to make sure
    # the same filename isn't used twice. Note: The file names will be sequential
    total = 0
    empty_csv(year, month, day, total, empty)
    total += empty
    correct_csv(year, month, day, total, correct)
    total += correct
    missing_header_csv(year, month, day, total, missing_header)
    total += missing_header
    missing_column_csv(year, month, day, total, missing_column)
    total += missing_column
    invalid_entry_csv(year, month, day, total, invalid_entries)
    total += invalid_entries
    duplicate_batch_id_csv(year, month, day, total, duplicate_batch_ids)
    total += duplicate_batch_ids
    incorrect_filename_csv(year, month, day, total, incorrect_filename)
    total += duplicate_batch_ids


# Asks the user for the date they'd like to generate files for and the type of each file they'd like,
# then runs the function to create those files
year = input("Enter Year: ")
month = input("Enter Month: ")
day = input("Enter Day: ")
empty = int(input("Number of empty files: "))
correct = int(input("Number of correct files: "))
missing_header = int(input("Number of files with a missing header: "))
missing_column = int(input("Number of files with a missing column: "))
invalid_entry = int(input("Number of files with an invalid entry: "))
duplicate_batch_id = int(input("Number of files with a duplicate batch_id: "))
incorrect_filename = int(input("Number of files with an incorrect filename: "))
csv_generator(year=year, month=month, day=day, correct=correct, empty=empty, missing_header=missing_header,
              missing_column=missing_column, duplicate_batch_ids=duplicate_batch_id, invalid_entries=invalid_entry,
              incorrect_filename=incorrect_filename)

