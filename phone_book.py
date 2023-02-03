phone = {}
for i in range(int(input())):
    num, name = input().split()
    if name not in phone:
        phone.setdefault(name, [num])
    else:
        phone[name] += [num]

for i in range(int(input())):
    name = input()
    if name in phone:
        print(*phone[name])
    else:
        print('Неизвестный номер')

for _ in range(int(input())):
    phone, name = input().split()
    phone_book.setdefault(name, []).append(phone)

for _ in range(int(input())):
    name = input()
    print(*phone_book.get(name, ['Неизвестный номер']))