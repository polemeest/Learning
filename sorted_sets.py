str = input()
mnoz = set(str)
for i in str:
    if i in mnoz:
        print(i, end='')
        mnoz.discard(i)


s = input()
print(''.join(sorted(set(s), key=s.index)))