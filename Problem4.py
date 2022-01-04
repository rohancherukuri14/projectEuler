maxNum = 999

def isPalindrome(n):
    return str(n)[::-1] == str(n)

maxProd = 0
for i in range(900, maxNum):
    for j in range(900, maxNum):
        prod = i * j
        if prod > maxProd:
            if isPalindrome(prod):
                maxProd = prod
print(maxProd)