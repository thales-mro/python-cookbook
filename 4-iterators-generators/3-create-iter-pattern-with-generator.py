# yield keyword transforms a function into a generator

def myrange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

def main():
    print(list(myrange(0, 1, 0.125)))

    for n in myrange(0, 4, 1.123):
        print(n)

    gen = myrange(4, 8, 1)
    print(gen)
    print(next(gen))
    print(next(gen))

if __name__ == "__main__":
    main()