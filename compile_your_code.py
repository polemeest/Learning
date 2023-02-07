def find_lines_len_more_6(file_name:str) -> int:
    lst = set()
    with open(file_name, encoding='utf-8') as file:
        for row in file.read().splitlines():
            for word in row.split():
                if word.lower() not in lst:
                    lst.add(word.lower())

    return len(lst)


def find_lines_len_more(file_name: str) -> int:
    with open(file_name, encoding='utf-8') as file_str:
        return len(set(file_str.read().strip().lower().split()))


print(find_lines_len_more_6('E:\\Downloads\\lorem.txt'))
