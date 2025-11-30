# l = [10, 20, 30, 40, 50]
l = input("enter list elements separated by space:").split()
l = [int(i) for i in l]
print(l)
l.append(30)
print(l)
print(l[-1])
print(l[1:4])
print(l[::-1])
print(20 in l)
print(l.count(30))
print(l.index(30))
print(l.index(30, 4, 6))
l.remove(30)
print(l)
print(l.pop(1))
print(l)
del l[2]
print(l)
del l[0:2]
print(l)
