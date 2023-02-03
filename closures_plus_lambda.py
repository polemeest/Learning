def multiply(n: int = 0) -> int:
    summ = n
    def plus(x: int) -> int:
        nonlocal summ
        a = summ * x
        return a
    return plus



f = lambda x: lambda y: x * y
f_1 = f(1)
print(f_1(5)) # 5

f_2 = multiply(2)
print("Умножение 2 на 5 =", f_2(5)) #10
print("Умножение 2 на 15 =", f_2(15)) #30
f_3 = multiply(3)
print("Умножение 3 на 5 =", f_3(5)) #15
print("Умножение 3 на 15 =", f_3(15)) #45