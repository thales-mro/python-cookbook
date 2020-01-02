import re

def main():
    print("strip() removes undesired characters for the beginning and the end of strings. rstrip() and lstrip() does for right and left sides, respectively.")
    s = '   hello world  \n'
    print(s.strip())
    print(s.rstrip())
    print(s.lstrip())

    t = '-----hello======='
    print(t.lstrip('-'))
    print(t.strip('-='))
    
    print("To replace in the middle of string: use replace() or regex")
    s = '  hello             world  \n'
    print(s.replace(' ', ''))
    print(re.sub(r'\s+', ' ', s))

if __name__ == "__main__":
    main()