prices = [6, 2, 8, 4, 5]
amounts = [10, 20, 30, 15, 20]

s = 0
for i in range(len(prices)):
    price = prices[i]
    amount = amounts[i]
    s += price * amount

print(s)