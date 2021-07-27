    
# Check to see if any of the columns of a row in a file are empty
# Will write to the log if this is the case
def ColCheck(csvFile):
    # Nesting could be made more efficient in the future
    for row in csvFile:
        for item in row:
            if (row[item] == ""):
                with open("log.txt","at") as log:
                    log.write("Missing columns on a row\n")



