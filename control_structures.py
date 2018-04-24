def nothing():
    pass


def simple():
    print(1)
    print(2)
    print(3)
    print(4)


def one_if(x):
    if x > 0:
        return 42
    return None


def one_if_else(x):
    if x > 0:
        return 42
    else:
        return None


def if_elif_else(x):
    if x > 0:
        return "kladny"
    elif x < 0:
        return "zaporny"
    else:
        return "nula"


def nested_if_else(x):
    if x > 0:
        return "kladny"
    else:
        if x < 0:
            return "zaporny"
        else:
            return "nula"


def max1(a, b, c):
    maximum = a

    if b > maximum:
        maximum = b

    if c > maximum:
        maximum = c

    return maximum


def max2(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def fibonacci1(i):
    x, y = 1, 1
    for i in range(i - 1):
        x, y = y, x + y
    return x


def fibonacci2(i):
    if i == 1 or i == 2:
        return 1
    return fibonacci2(i-1) + fibonacci2(i-2)


def factorial1(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result


def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n-1)


def factorial3(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
