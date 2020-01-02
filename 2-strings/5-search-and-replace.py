import re
from calendar import month_abbr

def replace_callback(m):
    mon_name = month_abbr[int(m.group(2))]
    return '{} {} {}'.format(m.group(1), mon_name, m.group(3))

def main():
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text.replace('yeah', 'yep'))
    
    text = "Today is 02/01/2020. In a week it will be 09/01/2020."
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(datepat.sub(r'\3-\2-\1', text))

    print(datepat.sub(replace_callback, text))

    print("If it is desired to know the number of replacements:")
    _, n = datepat.subn(r'\3-\2-\1', text)
    print(n)

if __name__ == "__main__":
    main()