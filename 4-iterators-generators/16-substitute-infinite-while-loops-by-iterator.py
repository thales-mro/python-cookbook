import sys

CHUNKSIZE = 8192

# for example, this function:
'''
def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)
'''

# can be substituted by this one:
def reader(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        #process_data(chunk)
        print("do whatever")

def main():
    f = open('/etc/passwd')
    for chunk in iter(lambda: f.read(10), ''):
        print(sys.stdout.write(chunk))
        print("--------------------")

if __name__ == "__main__":
    main()