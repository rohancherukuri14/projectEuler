def findPrimesUntilLim(lim):
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
    return primes

print(sum(findPrimesUntilLim(2000000)))