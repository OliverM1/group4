
# Checks to see if there are duplicated batch ids in the dictionary of the file
# Will write to log if this is the case
def batchIDCheck(csvFile):
    ids = []
    for row in csvFile:
        ids.append(row["batch_id"])
    removed = dict.fromkeys(ids)
    if (len(removed) != len(ids)):
        with open("log.txt","at") as log:
            log.write("Duplicate batch ids\n")