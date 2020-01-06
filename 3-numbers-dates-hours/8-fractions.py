from fractions import Fraction

def main():
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print(a, b, a + b, a * b)
    c = a * b
    print(c.numerator, c.denominator)
    print("To float:", float(c))
    print("To fraction:")
    x = 3.75
    y = Fraction(*x.as_integer_ratio())
    print(y)

if __name__ == "__main__":
    main()