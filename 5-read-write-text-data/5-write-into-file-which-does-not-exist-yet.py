import os

# alternative solution to the one presented in main():
def exists():
    if not os.path.exists('somefile'):
        with open('somefile', 'wt') as f:
            f.write('Hello!\n')
    else:
        print("File already exists!")

def main():
    with open('somefile', 'wt') as f:
        f.write('Hello!\n')

    with open('somefile', 'xt') as f:
        f.write('Hello!\n')

if __name__ == "__main__":
    main()