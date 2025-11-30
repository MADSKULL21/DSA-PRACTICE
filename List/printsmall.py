def getsmaller(l, x):
    small = []
    for y in l:
        if y < x:
            small.append(y)
    return small


x = int(input("enter number:"))
l = input("enter list elements separated by space:").split()
l = [int(i) for i in l]
print("elements smaller than", x, "are:", getsmaller(l, x))
