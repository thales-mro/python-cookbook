from collections import defaultdict

def main():
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(5)
    print(d)

    d2 = defaultdict(set)
    d2['r'].add(3)
    d2['r'].add(4)
    d2['s'].add(9)
    print(d2)

if __name__ == '__main__':
    main()