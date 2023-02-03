def create_actor(**kwargs) -> dict:
    '''принимает произвольное количество именованных аргументов и возвращает словарь с характеристиками актера'''
    dic = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46,
    }
    for k, v in kwargs.items():
        dic[k] = v
    return dic

def create_actor(**kwargs):
    d = {'name': 'Райан', 'surname': 'Рейнольдс', 'age': 46}
    if kwargs:
        d = d | kwargs
    return d

def create_actor(**kwargs):
    return {'name': 'Райан','surname': 'Рейнольдс','age': 46,} | kwargs

print(create_actor(height=190, movies=['Дедпул', 'Главный герой']))