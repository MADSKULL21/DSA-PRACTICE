# using slicing
"""l = [10, 20, 30, 40, 50]
new_l = l[::-1]
print(new_l)"""


# naive
def reverse_list(l):
    s = 0
    e = len(l) - 1
    while s < e:
        l[s], l[e] = l[e], l[s]
        s = s + 1
        e = e - 1
    return l


l = [10, 20, 30, 30, 40, 50]
print(reverse_list(l))
