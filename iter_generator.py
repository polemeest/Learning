shop = {}
[i.split(':') for i in iter(input, 'конец')]. 
while True:
    i = input()
    if i == 'конец':
        break
    shop[i.split(':')[0]] = int(i.split(':')[1])

for k in sorted(shop, key = lambda x: -shop[x]):
    print(k)