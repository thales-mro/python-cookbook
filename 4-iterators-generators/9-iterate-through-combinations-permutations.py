from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

def main():
    items = ['a', 'b', 'c']

    for p in permutations(items):
        print(p)

    for p in permutations(items, 2):
        print(p)

    for c in combinations(items, 3):
        print(c)

    for c in combinations(items, 2):
        print(c)

    for c in combinations_with_replacement(items, 3):
        print(c)


if __name__ == "__main__":
    main()
