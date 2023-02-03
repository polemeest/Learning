def only_one_positive(*args: int) -> bool:
    return len([i for i in args if i > 0]) == 1

def only_one_positive(*args):
    return sum(c > 0 for c in args) == 1






print(only_one_positive(-1, 0, -3, -3))