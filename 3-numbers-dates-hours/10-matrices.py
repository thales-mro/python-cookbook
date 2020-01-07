import numpy as np

def main():
    m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
    print(m)
    print(m.I)
    print(m.T)
    v = np.matrix([[2], [3], [4]])
    print(m*v)
    print(np.linalg.det(m))
    print(np.linalg.eigvals(m))
    print(np.linalg.solve(m, v))

if __name__ == "__main__":
    main()