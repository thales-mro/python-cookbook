import re

def main():
    line = "asdf fjdk; afed, fjek,asdf,     foo"
    print(re.split(r'[;,\s]\s*', line))
    print("With capture group:")
    print(re.split(r'(;|,|\s)\s*', line))
    print("Non capture group:")
    print(re.split(r'(?:;|,|\s)\s*', line))

if __name__ == "__main__":
    main()