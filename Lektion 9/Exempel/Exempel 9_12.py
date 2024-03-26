def calculate_total_price(prices):
    total_price = 0
    for price in prices:
        total_price += price
    return total_price

def apply_discount(prices, discount):
    discounted_prices = []
    for price in prices:
        discounted_price = price - discount
        discounted_prices.append(discounted_price)
    return discounted_prices

def main():
    prices = [10, 20, 30, 40, 50]
    discount = 5

    total_price = calculate_total_price(prices)
    print("Total price before discount:", total_price)

    discounted_prices = apply_discount(prices, discount)
    print("Discounted prices:", discounted_prices)

if __name__ == "__main__":
    main()
