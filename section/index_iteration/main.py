prices = [29.99, 45.50, 12.75, 38.20]

for index in range(len(prices)):
    updated_price = 0
    if index == 0:
        updated_price = prices[index] * (1-.1)
    elif index == 1:
        updated_price = prices[index] * (1-.2)
    elif index == 2:
        updated_price = prices[index] * (1-.15)
    elif index == 3:
        updated_price = prices[index] * (1-.05)
    else:
        updated_price = prices[index]

    prices[index] = updated_price
    print(f"Updated price for item {index}: ${updated_price:.2f} for each item.")
        