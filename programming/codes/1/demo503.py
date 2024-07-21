prices = [42, 46, 26, 27, 31, 
  24, 120, 26, 18, 23]

total = 0
count = 0
for i in range(len(prices)):
    if prices[i] <= 40:
        total += prices[i]
        count += 1

print(total, count, total / count)
