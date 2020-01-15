def main():
    with open('somefile.txt', 'at') as f:
        # make sure file is opened in text mode (binary mode will generate an error)
        print("Hey again!", file=f)

if __name__ == "__main__":
    main()