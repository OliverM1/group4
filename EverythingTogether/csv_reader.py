import csv

# Opens supplied CSV file and returns the Dictionary of the file
# As seen in the example


def fileToCSV(*, file_path):
    with open(file_path,"rt") as f:
        hold = f.readlines()
        csvReader = csv.DictReader(hold)
        f.close()
        return csvReader