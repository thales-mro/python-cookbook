def dedupe(items, key=None):
    seen = set()
    for item in items:
        value = item if key is None else key(item)
        if value not in seen:
            yield item
            seen.add(value)

def main():
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))
    d = [
        {'x': 1, 'y': 2},
        {'x': 1, 'y': 3},
        {'x': 1, 'y': 2},
        {'x': 2, 'y': 4}
    ]
    print(list(dedupe(d, key=lambda e: (e['x'], e['y']))))

if __name__ == "__main__":
    main()