def main():
    data = b'Hello World'
    print(data[0:5], data.startswith(b'Hello'), data.split())

    print("Indexing byte strings will return int not char:")
    print(data[0])

if __name__ == "__main__":
    main()