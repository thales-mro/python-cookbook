import heapq

# how two ordered files can be merged
def merge_ordered_files(in1, in2, out1):
    with open(in1, 'rt') as file1, \
         open(in2, 'rt') as file2, \
         open(out1, 'wt') as outf:

        for line in heapq.merge(file1, file2):
            outf.write(line)

def main():
    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]

    # iterables have to be previously ordered
    for c in heapq.merge(a, b):
        print(c)

if __name__ == "__main__":
    main()