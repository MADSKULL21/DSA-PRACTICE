def getSecMax(l):
    if len(l) <= 1:
        return None
    largest = l[0]
    second_largest = None
    for x in l[1:]:
        if x > largest:
            second_largest = largest
            largest = x
        elif x != largest:
            if second_largest is None or x > second_largest:
                second_largest = x
    return second_largest


l = [10, 20, 30, 15, 15, 20, 40, 40, 5]
print("second largest element is:", getSecMax(l))
