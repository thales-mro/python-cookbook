import re

def date_match(date):
    if re.match(r'\d+/\d+/\d+', date):
        print('yes')
    else:
        print('no')

def main():
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text.find('no'))

    date1 = '02/01/2020'
    date2 = '02 Jan, 2020'

    date_match(date1)
    date_match(date2)

    print("For multiple uses, it is good to compile the regex")
    datepat = re.compile(r'\d+/\d+/\d+')
    if datepat.match(date1):
        print("yes")
    else:
        print("no")

    if datepat.match(date2):
        print("yes")
    else:
        print("no")

    text = "Today is 02/01/2020. In a week it will be 09/01/2020."
    print(datepat.findall(text))

    print("Including capture groups (in parenthesis)")
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = datepat.match('26/09/1998')
    print(m)
    print(m.group(0), m.group(1), m.group(2), m.group(3), m.groups())

    print(datepat.findall(text))
    for month, day, year in datepat.findall(text):
        print('{}--{}--{}'.format(year, month, day))

    print("With finditer:")
    for m in datepat.finditer(text):
        print(m.groups())

    



if __name__ == "__main__":
    main()