oskar = {}
for i in range(int(input())):
    if (name := input()) not in oskar:
        oskar.setdefault(name, 1)
    else:
        oskar[name] += 1
print(*sorted(oskar.items(), key = lambda x: x[1])[-1], sep=', ')
print(*sorted(oskar.items(), key = lambda x: x[1])[0], sep=', ')

    d = {}
    for _ in range(int(input())):
        e = input()
    d[e] = d.get(e, 0) + 1
    kmax, kmin = max(d, key=d.get), min(d, key=d.get)
    print(kmax, d[kmax], sep=', ')
    print(kmin, d[kmin], sep=', ')