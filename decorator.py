def text_decor(func):
    def inner(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye!')

    return inner

@text_decor
def multiply(num1, num2):
    print(num1 * num2)

multiply(3, 5)


def repeater(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return inner


@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 7) # после этого распечатается две строки со значением 14
multiply(5, 3) # после этого распечатается две строки со значением 15


def double_it(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return inner



@double_it
def multiply(num1, num2):
    return num1 * num2

res = multiply(9, 4) # произведение 9*4=36, но декоратор double_it удваивает это значение
print(res)