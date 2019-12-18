from operator import itemgetter

def main():
    rows = [
        {'fname': 'Thales', 'lname': 'Oliveira', 'uid': 1003},
        {'fname': 'Paul', 'lname': 'Jones', 'uid': 1002},
        {'fname': 'Joseph', 'lname': 'Allen', 'uid': 1001},
        {'fname': 'Gustavo', 'lname': 'Oliveira', 'uid': 1004}
    ]

    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))

    print(rows_by_fname)
    print(rows_by_uid)

    rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
    print(rows_by_lfname)

if __name__ == "__main__":
    main()