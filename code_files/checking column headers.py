#checks column headers against given list and gives error message if format incorrect

import csv

#need to edit to fit in with other functions (and needs to be turned into a function)
with open("MED_DATA_20210701153942.csv") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter = ",")
    column_names = []
    for row in csv_reader:
        column_names.append(row)
        break

#not sure why I need two [ but seems to work
if column_names != [["batch_id","timestamp","reading1","reading2","reading3","reading4","reading5","reading6","reading7","reading8","reading9","reading10"]]:
    print("INVALID FILE")
