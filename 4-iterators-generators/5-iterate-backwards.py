class Countdown:
    def __init__(self, start):
        self._start = start

    def __iter__(self):
        n = self._start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self._start:
            yield n
            n += 1

def main():
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)

    f = open('example.txt')
    for line in reversed(list(f)):
        print(line, end='')

    cd = Countdown(5)
    for c in cd:
        print(c)

    #cd = Countdown(10)

    for c in reversed(cd):
        print(c)


if __name__ == "__main__":
    main()