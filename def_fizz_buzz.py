def generate_fizz_buzz_list(num):
    lst = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            lst.append('FizzBuzz')
        elif i % 3 == 0:
            lst.append('Fizz')
        elif i % 5 == 0:
            lst.append('Buzz')
        else:
            lst.append(i)
    return lst





def generate_fizz_buzz_list(n):
    return ["Fizz" * (not i % 3) + "Buzz" * (not i % 5) or i for i in range(1, n + 1)]