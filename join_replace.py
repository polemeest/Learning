def format_name_list(names: list[dict]) -> str:
    lst = [i['name'] for i in names]
    if len(lst) < 1:
        return ''
    elif len(lst) == 1:
        return lst[0]
    else:
        string = ''
        for i in lst:
            if i == lst[-2]:
                break
            else:
                string += i + ', '
        string += lst[-2]
        string += ' и '
        string += lst[-1]
        return string
    print(lst)

print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))


def format_namelist(dy):
    return ' и '.join(i['name'] for i in dy).replace(' и', ',', len(dy) - 2)