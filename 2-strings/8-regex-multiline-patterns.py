import re

def main():
    print("Dot operator does not take into consideration line breaks. Adaptation with non-capture group is needed.")
    comment = re.compile(r'/\*((?:.|\n)*?)\*/')
    text1 = '/* this is a comment in C */'
    text2 = '''/* this is a
        multiline comment in C */
    '''
    print(comment.findall(text1))
    print(comment.findall(text2))

    print("Or, using the DOTALL flag:")
    comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
    print(comment.findall(text1))
    print(comment.findall(text2))

if __name__ == "__main__":
    main()