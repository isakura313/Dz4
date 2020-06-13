def fact_rec(n, s):
    a = []
    if (n == 0 or n == 1) and (s == 1 or s > 6):
        return 1
    else:
        b = fact_rec(n ** (s), s - 1)
        a.append(b)
        return a


print(fact_rec(2, 5))




