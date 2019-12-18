def main():
    stocks = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'FB': 37.2,
        'HPQ': 10.75,
    }

    min_price = min(zip(stocks.values(), stocks.keys()))
    max_price = max(zip(stocks.values(), stocks.keys()))
    print(min_price, max_price)

    # it is equivalent to
    _ = stocks[min(stocks, key=lambda k: stocks[k])]


if __name__ == "__main__":
    main()