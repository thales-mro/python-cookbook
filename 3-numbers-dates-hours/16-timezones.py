from datetime import datetime
from pytz import timezone
from datetime import timedelta

def main():
    d = datetime(2012, 12, 21, 9, 30, 0)
    print(d)
    central = timezone('US/Central')
    loc_d = central.localize(d)
    print(loc_d)

    bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
    print(bang_d)
    #be cautious to summer time
    d = datetime(2013, 3, 10, 1, 45)
    loc_d = central.localize(d)
    later = central.normalize(loc_d + timedelta(minutes=30))
    print(later)
    #hint: always go to utc
    utc_d = loc_d.astimezone(timezone('UTC'))
    print(utc_d)

if __name__ == "__main__":
    main()