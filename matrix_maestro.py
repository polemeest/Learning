def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list[[int]]:
    mtx = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                mtx[i][j] = i + 1
            elif i > j and i != j:
                mtx[i][j] = down_fill
            elif j > i and i != j:
                mtx[i][j] = up_fill
    return mtx


def create_matrix(size: int=3, up_fill: int=0, down_fill: int=0) -> list[list[int]]:
    return [[down_fill] * i + [i + 1] + [up_fill] * (size - i - 1) for i in range(size)]


print(create_matrix(3, 5, 7))