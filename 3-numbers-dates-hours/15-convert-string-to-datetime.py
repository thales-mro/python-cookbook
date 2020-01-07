from datetime import datetime

#way faster solution than showed in main()
def parse_ymd(s):
    year_s, month_s, day_s = s.split('-') # only works if you know the string format
    return datetime(int(year_s), int(month_s), int(day_s))

def main():
    text = '2020-01-25'
    y = datetime.strptime(text, '%Y-%m-%d')
    z = datetime.now()
    diff = z - y
    print(diff)

    print(datetime.strftime(y, '%A %B %d, %Y'))
    print(parse_ymd(text))

if __name__ == "__main__":
    main()