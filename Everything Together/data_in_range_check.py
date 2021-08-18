#NEEDS TESTING AND CORRECTLY FORMATTING

#checks data entries are floats, 3dp and do not exceed 9.9
#prints INVALID FILE if not

import csv
import os


def datachecker(*, file_path):

    filename = os.path.basename(file_path)

    with open(file_path, 'rU') as data:
        reader = csv.reader(data)
        row = list(reader)

        count = 0

        for x in row:            
            for y in x:

                # Avoids csv entries that are not readings
                if count > 11 and count % 12 > 1:

                    # Checks if float
                    try:
                        z = float(y)
                    except:
                        with open("log.txt", "at") as log:
                            log.write(filename + " has invalid entries\n")
                        return True

                    # Checks if to 3dp and less than or equal to 9.9
                    if round(z, 3) != z or z > 9.9 or z < 0:
                        with open("log.txt", "at") as log:
                            log.write(filename + " has invalid entries\n")
                        return True

                count +=1

    return False
