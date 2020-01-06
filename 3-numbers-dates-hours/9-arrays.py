import numpy as np

def main():
    print("Lists are not suitable for math array operations:")
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    print(x * 2, x + y)

    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print(ax * 2, ax + ay, np.sqrt(ay), np.sin(ax))
    grid = np.zeros(shape=(10000, 10000), dtype=float)
    print(grid)
    grid += 10
    print(grid)
    print(np.sin(grid))
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a[:, 1])
    print(a + [100, 101, 102, 103])
    a[1:3, 1:3] += 10
    print(a)
    print(np.where(a < 10, a, 10))

if __name__ == "__main__":
    main()
