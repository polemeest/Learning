def find_keys(**kwargs) -> list:
    "Возвращает лист ключей, значения которых являются списками или кортежами"
    return sorted([i for i in kwargs if isinstance(kwargs[i], tuple | list)], key = str.lower)


