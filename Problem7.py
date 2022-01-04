import math
def upperBound(n):
    return int(n * (math.log(n) * math.log(math.log(n))))
def findPrimesUntilLim(n, lim):
    p_list = [True for i in range(lim+1)]
    primes = []
    start = 2
    while start**2 < lim:
        if p_list[start] == True:
            for i in range(start*start, lim+1, start):
                p_list[i] = False
        start += 1

    for i in range(2, lim+1):
        if p_list[i] == True:
            primes.append(i)
    return primes[n-1]

print(findPrimesUntilLim(10001, upperBound(10001)))
