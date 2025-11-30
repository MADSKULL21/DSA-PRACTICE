def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % 2 == 0:
            return False
    return True


def primeFactorize(n):
    for i in range(2, n + 1):
        if isPrime(i):
            x = i
            while n % x == 0:
                print(i)
                x = x * i


if __name__ == "__main__":
    num = int(input("Enter Number:"))
    primeFactorize(num)
