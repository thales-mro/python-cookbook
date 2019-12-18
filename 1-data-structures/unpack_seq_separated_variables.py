def unpack_sequences_diff_vars():
# it works for any type of sequence
    print("Tuple example:")
    p = (4, 5)
    x, y = p
    print(x, y)

    print("List example:")
    data = ['Thales', 50, 4.4, (2019, 12, 18)]
    string_val, int_val, double_val, tuple_val = data
    print(string_val, int_val, double_val, tuple_val)

    _, _, _, (year, month, day) = data
    print(day, month, year)

if __name__ == "__main__":
    unpack_sequences_diff_vars()
