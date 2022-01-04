def gcd(a, b): 
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def findLCM(n):
    lcm = 1
    for i in range(1, n+1):
        lcm = int((lcm * i)/gcd(lcm, i))
    return lcm
print(findLCM(20))