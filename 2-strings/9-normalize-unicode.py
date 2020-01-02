import unicodedata

def main():
    s1 = 'Spicy Jalape\u00f1o' # using only one character
    s2 = 'Spicy Jalapen\u0303o' # using a combination of characters
    print(s1, s2, s1 == s2, len(s1), len(s2))
    print("To normalize the representations:")
    print("\tNFC format: all symbols formed by one character")
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print("\t\t", t1, t2, t1 == t2, ascii(t1))
    print("\tNFD format: special symbols are combinations of characters")
    t3 = unicodedata.normalize('NFD', s1)
    t4 = unicodedata.normalize('NFD', s2)
    print("\t\t", t3, t4, t3 == t4, ascii(t3))

    print("Removing diacratical marks:")
    print(''.join(c for c in t3 if not unicodedata.combining(c)))

if __name__ == "__main__":
    main()