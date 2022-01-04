a = 1
b = 1
retSum = 0
while a <= 4000000:
    if a % 2 == 0:
        retSum += a
    a,b = b, a+b
print(retSum)