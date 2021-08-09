#NEEDS TESTING AND CORRECTLY FORMATTING

#checks data entries are floats, 3dp and do not exceed 9.9
#prints INVALID FILE if not

import csv
from extract_filename import extract_filename as extract


def datachecker(*, file_path):

    filename = extract(file_path=file_path)

    with open(file_path, 'rU') as data:
        reader = csv.reader(data)
        row = list(reader)

        count = 0
        brokenout = False

        for x in row:            
            for y in x:

                #avoids csv entries that are not readings
                if count > 11 and count % 12 > 1:

                    #checks if float
                    try:
                        z = float(y)
                    except:
                        with open("log.txt", "at") as log:
                            log.write(filename + " has invalid entries\n")
                        brokenout = True

                    #checks if to 3dp and less than or equal to 9.9
                    if round(z, 3) != z or z>9.9:
                        with open("log.txt", "at") as log:
                            log.write(filename + " has invalid entries\n")
                        brokenout = True

                #breaks inner loop
                if brokenout == True:
                    break

                count +=1

            #breaks outer loop
            if brokenout == True:
                break


                  
#datachecker('MED_DATA_20210701153942.csv')
