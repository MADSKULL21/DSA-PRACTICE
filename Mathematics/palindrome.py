x = int(input("Enter a number:"))
orignal_x = x
temp = 0
while x > 0:
    id = x % 10
    temp = (temp * 10) + id
    x = x // 10
if temp == orignal_x:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
