# Simple approach


"""def getMax(l):
for x in l:
    for y in l:
        if y > x:
            break
        else:
            return x
    return None
"""

# Efficient approach


def getMax(l):
    if not l:
        return None
    else:
        max = l[0]
        for i in l:
            if i > max:
                max = i
        return max


l = input("enter list elements separated by space:").split()
l = [int(i) for i in l]
print("maximum element is:", getMax(l))
