def main():
    text = "Hello world"
    print(text.ljust(20), '$')
    print(text.rjust(20), '$')
    print(text.center(20), '$')

    print("Char padding:")
    print(text.rjust(20, '='))
    print(text.center(20, '*'))

    print("With format():")
    print(format(text, '>20'), '$')
    print(format(text, '<20'), '$')
    print(format(text, '^20'), '$')

    print("Padding:")
    print(format(text, '=>20s'), '$')
    print(format(text, '=^20s'), '$')

    print("Format to multiple values:")
    print('{:>10s} {:>10s}'.format('Hello', 'World'))

    print("format() with numbers:")
    x = 1.2345
    print(format(x, '>10'))
    print(format(x, '^10.2f'))

if __name__ == "__main__":
    main()