from collections import ChainMap

def main():
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    c = ChainMap(a, b)
    print(c['x'])
    print(c['y'])
    print(c['z'])

if __name__ == "__main__":
    main()