n = int(input())
users = {}
for i in range(n):
    if (name := input()) not in users:
        users[name] = 0
        print('OK')
    elif name in users:
        users[name] += 1
        print(name + str(users[name]))



d = {}
for _ in range(int(input())):
    s = input()
    z = d.get(s, 0)
    print(f'{s}{z}' if z else 'OK')
    d[s] = z + 1