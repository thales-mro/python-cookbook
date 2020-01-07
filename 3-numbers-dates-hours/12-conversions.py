import datetime

def main():
    a = datetime.timedelta(days=2, hours=6)
    b = datetime.timedelta(hours=4.5)
    c = a + b
    print(a, b, c, sep="|")
    print(c.days)
    print(c.seconds)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)

    a = datetime.datetime(2012, 9, 23)
    print(a + datetime.timedelta(days=10))
    b = datetime.datetime(2012, 12, 21)
    d = b - a
    print(d.days)
    now = datetime.datetime.today()
    print(now)
    print(now + datetime.timedelta(minutes=10))

if __name__ == "__main__":
    main()