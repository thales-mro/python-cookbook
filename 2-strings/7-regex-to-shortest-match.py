import re

def main():
    str_pat = re.compile(r'\"(.*)\"')
    text1 = 'Computer says "no."'
    print(str_pat.findall(text1))
    text2 = 'Computer says "no." Phone says "yes."'
    print("Result will be wrong (greedy search, longest match):")
    print(str_pat.findall(text2))
    print("Add '?' to regex after '*' operator for shortest matching")
    str_pat = re.compile(r'\"(.*?)\"')
    print(str_pat.findall(text2))

if __name__ == "__main__":
    main()