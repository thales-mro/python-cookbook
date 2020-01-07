import random

def main():
    values = [1, 2, 3, 4, 5, 6]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.sample(values, 2))
    print(random.sample(values, 3))
    print(random.sample(values, 4))
    random.shuffle(values)
    print(values)
    random.shuffle(values)
    print(values)
    random.shuffle(values)
    print(values)
    print(random.randint(0, 10))
    print(random.randint(0, 10))
    print(random.randint(0, 10))
    print(random.random())
    print(random.random())
    print(random.random())
    print(random.getrandbits(4))
    print(random.getrandbits(32))


if __name__ == "__main__":
    main()