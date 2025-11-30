def checkifsorted(l):
    i = 1
    while i < len(l):
        if l[i] < l[i - 1]:
            return False
        i += 1
    return True


l = input("enter list elements separated by space:").split()
l = [int(i) for i in l]
if checkifsorted(l):
    print("Sorted")
else:
    print("Not sorted")
