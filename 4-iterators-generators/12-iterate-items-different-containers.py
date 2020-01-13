from itertools import chain

def main():
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']

    for x in chain(a, b):
        print(x)

if __name__ == "__main__":
    main()