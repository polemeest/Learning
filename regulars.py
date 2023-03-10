import re
from typing import Optional

# text = '''
# С227НА777
# КУ22777
# Т22В7477
# М227К19У9
# '''
# for n in text.split():
#     if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', n):
#         print(n, 'private')
#     elif re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', n):
#         print(n, 'taxi')
#     else:
#         print(n, 'fail')

# text3 = '''
# Он --- серо-буро-малиновая редиска!!
# >>>:->
# А не кот.
# www.kot.ru
# '''
#
# print(len(re.findall(r'[\w-]+\b', text3)))

# text4 = '''
# Иван Иванович!
# Нужен ответ на письмо от ivanoff@ivan-chai.ru.
# Не забудьте поставить в копию
# serge'o-lupin@mail.ru- это важно.
# '''
#
# text5 = 'boo@ya_ru -boo@ya.ru- foo№boo@ya.ru'
#
# for i in text5.split():
#     if re.findall(r'\w+@[^.\s]+.[^.\s]+', i):
#         print(i[:-1] if i.endswith(('.', '-', ' ')) else i)


# text6 = '''
# Уважаемые! Если вы к 09:00 не вернёте
# чемодан, то уже в 09:00:01 я за себя не отвечаю.
# PS. С отношением 25:50 всё нормально!
# '''
#
# print(re.sub(r'[0-1][0-9](?:[:-][0-9]{2})+|[2][0-4](?:[:-][0-9]{2})+', '(TBD)', text6))


# text7 = '''
# 1.2
#   1.
#     1.0e-55
#       e-12
#   6.5E
#         1e-12
#   +4.1234567890E-99999
#   7.6e+12.5
#    99
# '''
# '''
# 1.2 is legal.
# 1. is illegal.
# 1.0e-55 is legal.
# e-12 is illegal.
# 6.5E is illegal.
# 1e-12 is legal.
# +4.1234567890E-99999 is legal.
# 7.6e+12.5 is illegal.
# 99 is illegal.
# '''
#
# for i in text7.split():
#     if re.fullmatch(r'[-+]?\d+\.[\deE]+[-+][\d]+|[-+]?\d+\.[\d]+|\d+[eE](?:[-+]|\d)+', i):
#         print(i, 'is legal')
#     else:
#         print(i, 'is illegal')

# text8 = '''
# Это курс информатики соответствует ФГОС и ПООП,
# это подтверждено ФГУ ФНЦ НИИСИ РАН
# '''
#
# print(re.findall(r'[А-Я]+(?:\s[А-Я]+)+|[А-Я][А-Я]+', text8))

# text9 = '''Было закуплено 12 единиц техники
# по 410.37 рублей.'''
#
# def change(match: Optional) -> str:
#     if '.' in match[0]:
#         return str(float(match[0]) ** 3)
#     return str(int(match[0]) ** 3)
#
# print(re.sub(r'(\d+.?\d+)', change, text9))


# text10 = '''микоян авиацию снабдил алкоголем,
# народ доволен работой авиаконструктора'''
#
# print(*(i.upper() for i in re.findall(r'\b\w', text10)), sep='')


# text11 = '''Жизнь скоротечна… / Думает ли об этом / Маленький мальчик.'''
# pattern = r'[АЯЕУОИЫЭЮаяеуоиыэю]'
# lst = text11.split(' / ')
# for i, string in enumerate(lst, 1):
#     if len(lst) != 3:
#         print('Не хайку. Должно быть 3 строки.')
#         break
#     norm = 5
#     if string == lst[1]:
#         norm = 7
#     if (slog := len(re.findall(pattern, string))) != norm:
#         print(f'Не хайку. В {i} строке слогов не {norm}, а {slog}.')
#         break
# else:
#     print('Хайку!')




