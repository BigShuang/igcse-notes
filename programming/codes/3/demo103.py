def calSquareSum(n):
    s = 0
    for i in range(n):
        s += (i+1) * (i+1)

    print("The sum of the squares of 1->", n,":", s)

calSquareSum(10)
calSquareSum(100)
calSquareSum(1000)