x = int(input("Enter N:"))
res = 0
while x > 0:
    x = x // 10
    res = res + 1
print("Count of digits is:", res)
