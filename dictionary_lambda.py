drivers, sample = {}, input()
while sample != 'конец':
    name, point = sample.split(', ')
    drivers.setdefault(name, []).append(int(point))
    sample = input()
for k, v in drivers.items():
    vv = sum(v) / len(v)
    drivers[k] = vv

for k, v in sorted(drivers.items(), key=lambda x: (-x[1], x[0])):
    print(k, v)


-----------------------------------------------------------------------------------------------------------------------
names = {}

for data in iter(input, 'конец'):
    name, n = data.split(', ')
    names.setdefault(name, []).append(int(n))

for key in names:
    names[key] = sum(names[key]) / len(names[key])

names = sorted(names.items(), key=lambda i: (-i[1], i[0]))

for rating in names:
    print(*rating)
