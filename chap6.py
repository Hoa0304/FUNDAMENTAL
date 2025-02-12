import math
def area(radius):
    return math.pi * radius**2

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    return math.sqrt(dsquared)

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))
# lắp ráp hàm 

def is_divisible(x, y):
    return x % y == 0

def factorial(n):
    if not isinstance(n, int):
        print('Giai thừa chỉ được định nghĩa cho các số nguyên.')
        return None
    elif n < 0:
        print('Giai thừa không được định nghĩa cho số nguyên âm.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y + 3, x + y))
