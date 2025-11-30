# Naive approach


"""def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % 2 == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input("Enter Number:"))
    if isPrime(num):
        print(num, " is a prime number")
    else:
        print(num, " is not a prime number")
"""
# Efficient approach


def isPrimeEfficient(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    num = int(input("Enter Number:"))
    if isPrimeEfficient(num):
        print(num, " is a prime number")
    else:
        print(num, " is not a prime number")
