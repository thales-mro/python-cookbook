import os
import textwrap

def main():
    text = "Hello, this is a kind of lorem ipsum done my myself. I tis expected to be long enough to look weird when trying to display it only using the max space of columns in the terminal. textwrap comes to mitigate this issue."

    print(textwrap.fill(text, 70))
    print(textwrap.fill(text, 30))

    print("Number of columns in the terminal:", os.get_terminal_size().columns)

    print(textwrap.fill(text, 40, initial_indent='    '))
    print(textwrap.fill(text, 40, subsequent_indent='******'))

if __name__ == "__main__":
    main()