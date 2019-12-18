from collections import namedtuple

def main():
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscriber('thales@itaporanga.com', '2012-10-19')
    print(sub)
    print(sub.addr, sub.joined)
    # still works as a tuple
    print(len(sub))
    addr, joined = sub
    print(addr, joined)

if __name__ == "__main__":
    main()