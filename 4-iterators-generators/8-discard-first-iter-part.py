from itertools import dropwhile
from itertools import islice

def main():
    with open('example2.txt') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')

    # if the number of elements to be not considered is known:
    items = ['a', 'b', 'c', 1, 3, 4, 12]
    for x in islice(items, 3, None):
        print(x)


if __name__ == "__main__":
    main()