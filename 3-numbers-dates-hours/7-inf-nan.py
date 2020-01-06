import math

def main():
    a = float('inf')
    b = float('-inf')
    c = float('nan')
    print(a, b, c)
    print("Test if these values are present:")
    print(math.isinf(a))
    print(math.isnan(c))

    print("Inf and nan are propagated through math operations:")
    print(a + 45, a * 10, 10/a, 1/b)
    print(c + 23, c / 2)

    print("Some operations result in NaN:")
    print(a/a, a + b)

    print("Can't compare two NaNs:")
    d = float('nan')
    print(c == d, c is d)

if __name__ == "__main__":
    main()