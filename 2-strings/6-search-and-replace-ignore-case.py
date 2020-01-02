import re

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        return word
    return replace

def main():
    text = "UPPER PYTHON, lower python, Mixed Python"
    print(re.findall('python', text, flags=re.IGNORECASE))
    print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
    print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

if __name__ == "__main__":
    main()