def getevenodd(l):
    even = []
    odd = []
    for x in l:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even, odd


l = [10, 21, 22, 24, 25, 45, 40]
even, odd = getevenodd(l)
print("Even:", even)
print("Odd:", odd)
