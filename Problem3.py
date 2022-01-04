num = 600851475143
maxFactor  = 0
while (num % 2 == 0):
    maxFactor = 2
    num /= 2

for i in range(3, int(num ** 0.5)):
    while(num % i == 0):
        maxFactor = i
        num /= i

if num > 2:
    maxFactor = num

print(maxFactor)