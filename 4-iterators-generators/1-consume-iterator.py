def main():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

    # in case you don't want the try/except structure:
    '''
    with open('/etc/passwd') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')
    '''
    items = [1, 2, 3]
    it = iter(items)
    print(next(it))
    print(next(it))
    print(next(it))

if __name__ == "__main__":
    main()