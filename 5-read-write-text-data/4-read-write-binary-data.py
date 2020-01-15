import array

def main():
    with open('somef.bin', 'wb') as f:
        text = 'Hello bin world!\n'
        f.write(text.encode('utf-8'))

    with open('somef.bin', 'rb') as f:
        data = f.read()
        print(data)
        print(data[0])
        text = data.decode('utf-8')
        print(text)
        print(text[0])

    # cool thing: C structures do not have to be encoded to be written in binary files:
    nums = array.array('i', [1, 2, 3, 4])
    with open('data.bin', 'wb') as f:
        f.write(nums)

    # binary data can be directly read to a subjacent memory:
    a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
    with open('data.bin', 'rb') as f:
        f.readinto(a)
    print(a)

if __name__ == '__main__':
    main()