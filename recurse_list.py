def flatten(lst: list) -> list:
    lst1 = []
    for i in lst:
        if type(i) != list:
            lst1.append(i)
        else:
            lst1 += flatten(i)
    return lst1













print(flatten([[[[9]]], [1, 2], [[8]]]))
