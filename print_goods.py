def print_goods(*args) -> None:
    no = 1
    for index, name in enumerate(args, 1):
        if type(name) == str and name != '':
            print(f'{no}. {name}')
            no += 1
    else:
        if no == 1:
            print('Нет товаров')

def print_goods(*args):
    out = [v for v in args if isinstance(v, str) and v]
    if len(out) > 0:
        for i, v in enumerate(out, 1):
            print(f'{i}. {v}')
    else:
        print('Нет товаров')


print_goods(1, True, 'Грушечка', '', 'Pineapple')