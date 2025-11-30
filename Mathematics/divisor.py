# Naive approach


"""def printDivisor(n):
Divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        Divisors.append(i)
return Divisors
"""

# Efficient approach


def printDivisor(n):
    Divisor = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
            Divisor.append(i)
            if i != n / i:
                print(n / i)
                Divisor.append(n / i)
        i += 1
    return Divisor


if __name__ == "__main__":
    n = int(input("enter number:"))
    print("the divisors are:\n", printDivisor(n))
