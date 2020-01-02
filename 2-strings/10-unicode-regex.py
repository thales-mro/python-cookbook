import re

def main():
    print('"\\d" already recognizes unicode digits')
    num = re.compile(r'\d+')
    print(num.match('123'))

    arabic_digits = "\u0661\u0662\u0663"
    print(arabic_digits)
    print(num.match(arabic_digits))

if __name__ == "__main__":
    main()