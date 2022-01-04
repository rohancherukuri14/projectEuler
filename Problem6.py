def sumOfTheSquares(n):
    retSum = 0
    for i in range(1, n+1):
        retSum += i*i
    return retSum

def squareOfTheSum(n):
    return ((n*(n+1))/2) ** 2

print(squareOfTheSum(100) - sumOfTheSquares(100))