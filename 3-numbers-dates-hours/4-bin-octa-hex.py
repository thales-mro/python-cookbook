def main():
    x = 1234
    print(bin(x))
    print(oct(x))
    print(hex(x))
    print("Without prefix:")
    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))
    print("Negative (unsigned):")
    x = -1234
    print(format(2**32 + x, 'b'))
    print(format(2**32 + x, 'o'))
    print(format(2**32 + x, 'x'))
    print("base 2^n to 10:")
    print(int('4d2', 16))

if __name__ == "__main__":
    main()