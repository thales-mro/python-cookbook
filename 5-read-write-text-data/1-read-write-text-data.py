def main():
    # usage of 'with' instruction determines a context block. Using 'with' for file manipulation allows to skip the file.close() instruction

    # reads file as unique string:
    with open('hello.txt', 'rt') as f:
        data = f.read()
        print(data)

    #iterate through file lines:
    with open('hello.txt', 'rt') as f:
        for line in f:
            print("line", line, sep=':')

    # write in file (with override):
    with open('somefile.txt', 'wt') as f:
        f.write("oi!\n")
        f.write("hello!")

    # write in file (with append):
    with open('somefile.txt', 'at') as f:
        f.write('\nbreaking news---')

    # redirect print instruction to file:
    with open('somefile.txt', 'at') as f:
        print('\nGood programmer found unemployed', file=f)

    # specifying encoding:
    with open('sample.txt', 'rt', encoding='latin-1') as f:
        print(f.read())

    # avoiding encoding errors:
    f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
    print(f.read())
    f.close()
    f = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
    print(f.read())
    f.close()

if __name__ == "__main__":
    main()