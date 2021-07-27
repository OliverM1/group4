# Enter date and get right format for CSV_Generator

def year_format(year, month, day):
    """Takes day, month and year and puts the date into the proper format for MED_DATA_YYYYMMDDHHMMSS.csv"""
    if int(month) < 10:
        month = "0" + str(month)
    if int(day) < 10:
        day = "0" + str(day)
    year = str(year)
    return year + month + day

def time_format(time_seconds):
    """TAkes the time in seconds and converts it into hours, minutes and seconds, then puts in the proper format for MED_DATA_YYYYMMDDHHMMSS.csv"""
    hour_2 = divmod(time_seconds, 36000)[0]
    time = divmod(time_seconds, 36000)[1]
    hour_1 = divmod(time, 3600)[0]
    time = divmod(time, 3600)[1]
    minute_2 = divmod(time, 600)[0]
    time = divmod(time, 600)[1]
    minute_1 = divmod(time, 60)[0]
    time = divmod(time, 60)[1]
    second_2 = divmod(time, 10)[0]
    second_1 = divmod(time, 10)[1]

    return str(hour_2) + str(hour_1) + str(minute_2) + str(minute_1) + str(second_2) + str(second_1)
