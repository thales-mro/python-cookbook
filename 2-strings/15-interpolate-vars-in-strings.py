import sys

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

def main():
    s = '{name} has {n} messages'
    print(s.format(name='Thales', n=14))

    name = 'Thales Oliveira'
    n = 48
    print(s.format_map(vars()))

    print("It also works with instances:")
    person = Info('Thales O.', 56)
    print(s.format_map(vars(person)))

    print("Deal with missing values:")
    del n
    print(s.format_map(safesub(vars())))

    print("With frame hack:")
    print(sub('Hello {name}'))
    print('Your favorite color is {color}')


if __name__ == "__main__":
    main()