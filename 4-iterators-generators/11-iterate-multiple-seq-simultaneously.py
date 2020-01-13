from itertools import zip_longest

def main():
    xpts = [1, 2, 3, 4, 5, 6, 7]
    ypts = [10, 11, 12, 13, 14, 15, 16]

    for x, y in zip(xpts, ypts):
        print(x, y)

    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']

    for i in zip(a, b):
        print(i)

    for i in zip_longest(a, b, fillvalue=0):
        print(i)

    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]

    s = dict(zip(headers, values))

    print(s)

    b = [10, 11, 12]
    c = ['x', 'y', 'z']

    for i in zip(a, b, c):
        print(i)

    print(list(zip(a, b)))        

if __name__ == "__main__":
    main()