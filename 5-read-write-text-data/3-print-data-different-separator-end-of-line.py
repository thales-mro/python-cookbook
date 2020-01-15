def main():
    print('ACME', 50, 91.5)
    print('ACME', 50, 91.5, sep=',')
    print('ACME', 50, 91.5, sep=',', end="!!\n")

    for i in range(5):
        print(i)

    for i in range(5):
        print(i, end=' ')
    print()

    # using str.join() only works if arguments are strings
    str_list = ['ACME', '50', '91.5']
    print(','.join(str_list))
    # to work with other data types:
    r_list = ['ACME', 50, 91.5]
    print(','.join(str(x) for x in r_list))

if __name__ == "__main__":
    main()