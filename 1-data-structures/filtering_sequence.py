def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

def main():
    # list comprehension
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    print([n for n in mylist if n > 0])
    # or (using generator)
    pos = (n for n in mylist if n > 0)
    for x in pos:
        print(x)
    # or (using filter() function)
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    ivals = list(filter(is_int, values))
    print(ivals)

if __name__ == "__main__":
    main()