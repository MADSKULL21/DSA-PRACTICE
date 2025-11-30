def fact(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res


if __name__ == "__main__":
    num = int(input("Enter Number:"))
    print("Factorial of", num, " is:", fact(num))
