# course
"""def remove_duplicate(arr, n):
    temp = [0] * n
    temp[0] = arr[0]
    res = 1
    for i in range(1, n):
        if temp[res - 1] != arr[i]:
            temp[res] = arr[i]
            res += 1
    for i in range(res):
        arr[i] = temp[i]
    return res


l = [10, 20, 20, 30, 30, 40, 50]
res = remove_duplicate(l, len(l))
print("Count of unique elements:", res)
print("Array after removing duplicates:", l[:res])
"""

# chatgpt
"""def remove_duplicates(nums):
    seen = set()
    result = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


l = [10, 20, 20, 30, 30, 40, 50]
print("Array after removing duplicates:", remove_duplicates(l))
"""

# optimized


def remove_duplicate(arr, n):
    res = 1
    for i in range(1, n):
        if arr[res - 1] != arr[i]:
            arr[res] = arr[i]
            res += 1
    return res


l = [10, 20, 20, 30, 30, 40, 50]
res = remove_duplicate(l, len(l))
print("Count of unique elements:", res)
print("Array after removing duplicates:", l[:res])
