with open('E:\\Downloads\\words.txt', encoding='utf-8') as file_str:
    words = set()
    for word in file_str.read().strip().upper().split():
        if word not in words and word.endswith('ЕЯ'):
            words.add(word)
    print(*sorted(words, key=lambda x: (len(x), x)), sep='\n')



with open('words.txt', encoding='utf-8') as i:
    plenty = {w for s in i for w in s.upper().split() if w.endswith('ЕЯ')}
    print('\n'.join(sorted(sorted(plenty), key=len)))