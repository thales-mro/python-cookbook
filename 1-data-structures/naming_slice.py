def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    SL1 = slice(0, 2)
    SL2 = slice(4, 8)
    print(SL1, SL2)
    print(l[SL2])

if __name__ == "__main__":
    main()