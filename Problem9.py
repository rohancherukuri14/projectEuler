for a in range(0,500):
    for b in range(0, 500):
        c_squared = a**2 + b ** 2
        c = c_squared ** (0.5)
        if c == int(c):
            if a+b+c == 1000:
                print( a*b*c)
                exit(0)