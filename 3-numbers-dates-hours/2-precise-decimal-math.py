from decimal import Decimal, localcontext

def main():
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a + b, 4.2 + 2.1)
    print(a + b == Decimal('6.3'), 4.2 + 2.1 == 6.3)

    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a/b)
    with localcontext() as ctx:
        ctx.prec = 3
        print(a/b)
    with localcontext() as ctx:
        ctx.prec = 50
        print(a/b)

if __name__ == "__main__":
    main()