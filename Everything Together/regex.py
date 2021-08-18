from datetime import date

def today_date():
    today = str(date.today())
    today = today.replace("-","")
    return today

def make_regex(date_to_add):
    base = "^MED_DATA_YYYYMMDD[0-9][0-9][0-9][0-9][0-9][0-9].csv$"
    return base.replace("YYYYMMDD",date_to_add)
