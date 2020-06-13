def cikl(n):
    a = []
    if n == 0 or n == 1:
        return 1
    else:

        for i in range(2, 6):
            b = n**i
            a.append(b)
        return a

print(cikl(5))