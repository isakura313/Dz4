chisla = []

def recusia(n, s, start):

    if (start == s):
        return
    else:
        chislo = n ** start
        chisla.append(chislo)
        start += 1
        recusia(n, s, start)
        return chisla



print(recusia(2, 5, 1))




