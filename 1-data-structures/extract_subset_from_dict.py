def main():
    prices = {
        'ACME': 45.323,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.2,
        'FB': 10.75
    }

    d1 = { key:value for key, value in prices.items() if value > 200 }
    print(d1)

    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key:value for key, value in prices.items() if key in tech_names}
    print(p2)


if __name__ == "__main__":
    main()