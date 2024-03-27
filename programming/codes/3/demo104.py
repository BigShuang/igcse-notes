def calSquareSum(n):
    s = 0
    for i in range(n):
        s += (i+1) * (i+1)

    return s

s1 = calSquareSum(10)
s2 = calSquareSum(100)
s3 = calSquareSum(1000)

print("s2 / s1:", round(s2 / s1, 1))
print("s3 / s2:", round(s3 / s2, 1))