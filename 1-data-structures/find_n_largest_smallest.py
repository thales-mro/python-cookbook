import heapq

def find_largest_smallest():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    grades = [
        {'name': "Thales", 'course': "Introduction to Computer Vision", 'grade': 9.1},
        {'name': "Mateus", 'course': "Introduction to Digital Image Processing", 'grade': 9.2},
        {'name': "Rodrigues", 'course': "Mobile Robotics", 'grade': 9.8}
    ]

    better = heapq.nlargest(2, grades, key=lambda s: s['grade'])
    worse = heapq.nsmallest(2, grades, key=lambda s: s['grade'])

    print(worse)
    print(better)

if __name__ == "__main__":
    find_largest_smallest()