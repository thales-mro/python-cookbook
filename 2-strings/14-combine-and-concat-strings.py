def main():
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print(''.join(parts))
    print(','.join(parts))

    a = "Oi"
    b = "Thales"
    c = "here"

    print(a, b, c, sep=',')
    print('{} {} {}'.format(a, b, c))

if __name__ == "__main__":
    main()