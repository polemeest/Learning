counter = {}
for i in (n := input().lower()):
    if i.isalpha():
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
print(counter)






s = input().lower()
d = {i: s.count(i) for i in s if i.isalpha()}
print(d)