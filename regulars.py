def longest_word_in_file(file_name):
    string = ''
    with open(file_name, encoding='utf-8') as file:

        lst = [i.replace(',', '').replace('.', '').split() for i in file.readlines()]
        for i in lst:
            for j in i:
                if len(j) >= len(string):
                    string = j
    return string

print(longest_word_in_file('venv/text.txt'))


from re import split

def longest_word_in_file(filename):
    with open(filename, 'r') as f:
        return max(split('\W+', f.read())[:: -1], key=lambda x: len(x))

    from string import punctuation

    def longest_word_in_file(file_name):
        with open(file_name, encoding='utf-8') as f:
            words = [*map(lambda x: x.strip(punctuation), f.read().split())]
            return max(words[::-1], key=lambda x: len(x))