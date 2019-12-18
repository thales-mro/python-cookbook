def unpack_arbitrary_size():
    list_example = [10, 8, 3, 5, 7, 7, 2, 1, 10, 4]
    # seq, in this case, will always be a list, even if it is empty
    *seq, last = list_example
    print(seq, last)
    print(sum(seq), len(seq))

if __name__ == "__main__":
    unpack_arbitrary_size()
