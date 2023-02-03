def factorial(n):
    pt = 1
    for i in range(1, n +1):
        pt *= i
    return pt

def trailing_zeros(n):
    num = str(factorial(n))[::-1]
    lst = []
    for i in num:
        if int(i) == 0:
            lst.append(i)
        else:
            break
    return len(lst)

from math import factorial as f

def trailing_zeros(n: int) -> int:
    sn = str(f(n))
    return len(sn) - len(sn.rstrip('0'))

print(factorial(6))
print(trailing_zeros(20))