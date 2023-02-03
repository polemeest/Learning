def check_password(passw):
    l = len(passw)
    dig = len([int(i) for i in passw if i.isdigit() == True])
    H = ''
    word = False
    for i in passw:
        if i in '!@#$%*':
            word = True
        if i != i.lower():
            H += i
    if l > 9 and word == True and dig > 2 and H != '':
        print("Perfect password")

    else:
        print("Easy peasy")


import re


def check_password(n):
    rule1 = len(re.findall("\d", n)) >= 3
    rule2 = bool(re.search("[A-Z]", n))
    rule3 = bool(re.search("[!@#$%*]", n))
    rule4 = len(n) >= 10
    if rule1 and rule2 and rule3 and rule4:
        print('Pefrect password')
    else:
        print('Easy peasy')

def  check_password(p):
    numbers = [i for i in p if i.isdigit()]
    char = [i for i in p if i.isupper()]
    symb = [i for i in p if i in  "!@#$%*"  ]

    print("Pefrect password" if len(numbers) >= 3 and len(char) >= 1 and len(symb) >= 1 and len(p) >= 10 else "Easy peasy")


check_password('Qwerty1734!')