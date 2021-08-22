from ftp_client import ftpclient
import sys
import re
from regex import today_date,make_regex
from gui import show_gui
from check_runner import run_checks
from cleanup import cleanup

def terminal_or_ui(argv):
    args = len(argv)
    if (args == 0):
        show_gui()
        pass
    elif ((args < 2) or (args > 3) ):
        #If args are passed it needs to be 
        # ip port optionally date
        # so error message here
        error_message()    
    elif (args == 2):
        #check argv
        #grab date and build regex for this

        if (not( (ip_check(argv[0])) and (port_check(int(argv[1]))))):
            error_message()
            exit()
        else:
            today = today_date()
            regexstr = make_regex(today)
            grab_files(ip=argv[0],port=int(argv[1]),regex=regexstr)

    elif (args == 3):
        if (not( (ip_check(argv[0])) and (port_check(int(argv[1]))) and (date_check(argv[2])()))):
            error_message()
            exit()
        else:
            regexstr = make_regex(argv[2])
            grab_files(ip=argv[0],port=int(argv[1]),regex=regexstr)

def error_message():
        print("Requires 0 args for GUI mode")
        print("Requires 2 or 3 args for automated download")
        print("Format is - IP, PORT, (optionally) Date (dd-mm-yyyy) ")

def ip_check(ip):
    IP_PATTERN = re.compile((
    "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}"
    "(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    ))
    return bool(re.match(IP_PATTERN,ip))

def port_check(port):
    return ((port > 0) and (port < 65536))

def date_check(supplied_date):
    DATE_PATTERN = re.complie("^\d\d\d\d\d\d\d\d$")
    return bool(re.match(DATE_PATTERN,supplied_date))

def grab_files(*,ip,port,regex):
    ftp = ftpclient(regex_str=regex,server_ip=ip,port=port)
    ftp.connect()
    files = ftp.match()
    print(f"Downloading {files} files")
    ftp.download()
    print("Finished")
    ftp.disconnect()
    run_checks()
    cleanup()

terminal_or_ui(sys.argv[1:])   