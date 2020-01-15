from collections import Iterable

# with yield from
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

# without yield from
def flatten2(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x

def main():
    items = [1, 2, [3, 4, [5, 6], 7], 8]

    for x in flatten(items):
        print(x)

if __name__ == "__main__":
    main()