# Reverse digits of an integer


def reverse_digit(n):
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    return reversed_n


result = reverse_digit(1234)
print("The reverse of the given digit is", result)
