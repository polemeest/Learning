# # функция merge_two_list должна объединить два списка
def merge_two_list(a, b):
    sort1 = []
    N, M = len(a), len(b)
    i = j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            sort1.append(a[i])
            i += 1
        else:
            sort1.append(b[j])
            j += 1

    sort1 += a[i:] + b[j:]
    return sort1

# # функция merge_sort должна выполнить сортировку

def merge_sort(s):
    a, b = s[:len(s) // 2], s[len(s) // 2:]
    if len(a) > 1:
        a = merge_sort(a)
    if len(b) > 1:
        b = merge_sort(b)

    return merge_two_list(a, b)

b = [6, 2, 19, 5, 10, 7, 11, -8, -11, -29, 4]
print(merge_sort(b))
a = [9, 5, -3, 4, 7, 8, -8]
