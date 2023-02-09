def count_strings(*args) -> int:
    "Возвращает количество строк из кортежа переданных аргументов"
    return len([i for i in args if isinstance(i, str) == True])

print(count_strings(1, 2, 'hello', [2, 3, 4], True))



