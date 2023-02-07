from typing import Generator
def gen_fibonacci_numbers(num: int, n_1 = 0, n_2 = 1) -> Generator[int, int, None]:
    "Генерирует последовательность чисел Фибоначчи"
    yield n_2
    for i in range(1, num):
        yield n_1 + n_2
        n_1, n_2 = n_2, n_1 + n_2

for i in gen_fibonacci_numbers(5):
    print(i)


#
# def gen_fibonacci_numbers(n, a=1, b=1):
#     for i in range(n):
#         yield a
#         a, b, = b, a + b