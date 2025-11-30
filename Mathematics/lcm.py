# Naive approach


"""def lcm(a, b):
    res = max(a, b)
    while res % a != 0 or res % b != 0:
        res = res + 1
    return res


if __name__ == "__main__":
    a = int(input("Enter number 1:"))
    b = int(input("enter number 2:"))
    print("LCM=", lcm(a, b))
"""

# Efficient approach


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm_efficient(a, b):
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    a = int(input("Enter number 1:"))
    b = int(input("enter number 2:"))
    print("LCM (Efficient) =", lcm_efficient(a, b))
