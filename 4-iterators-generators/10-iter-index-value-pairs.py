def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except IndexError as er:
                print('Line {}: Parse error: {}'.format(lineno, er))
            except ValueError as er2:
                print('Line {}: Parse error 2: {}'.format(lineno, er2))

def main():
    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list):
        print(idx, val)

    for idx, val in enumerate(my_list, 1):
        print(idx, val)

    parse_data('example2.txt')

    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    for n, (x, y) in enumerate(data):
        print(n, x, y)

if __name__ == "__main__":
    main()