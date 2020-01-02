def main():
    name = "Thales"

    print(name.startswith('Tha'))
    print(name.endswith('is'))

    # for multiple options, must use a tuple
    print(name.endswith(tuple(['is', 'les'])))

if __name__ == "__main__":
    main()