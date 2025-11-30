"""def avg(l):
sum = 0
for x in l:
    sum = sum + x
n = len(l)
return sum / n
"""


def avg(l):
    return sum(l) / len(l)


l = input("Enter numbers separated by space:").split()
l = [int(i) for i in l]
print("average is:", avg(l))
