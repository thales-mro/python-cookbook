import cmath

def main():
    a = complex(2, 4)
    b = 3 - 5j
    print(a)
    print(b)
    print(a.real, b.imag, a.conjugate())
    print(a + b, a - b, a / b, a * b)
    print(cmath.sin(a), cmath.cos(a), cmath.exp(a))
    print(cmath.sqrt(-1))

if __name__ == "__main__":
    main()