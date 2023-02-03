def get_word_indices(strings: list[str]) -> dict:
    dic = {}

    def add_to_dic(word, ind):
        if word.lower() not in dic:
            dic[word.lower()] = [ind]
        else:
            dic[word.lower()] += [ind]

    for index, lst in enumerate(strings):
        for word in lst.split():
            add_to_dic(word, index)
    return dic


def get_word_indices(strings: list[str]) -> dict:
    d = {}
    for i, k in enumerate(strings):
        for j in k.lower().split():
            d.setdefault(j, []).append(i)
    return d



print(get_word_indices(['This is a string',
                         'test String',
                         'test',
                         'string']))