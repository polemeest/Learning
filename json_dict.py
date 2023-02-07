# import json
# with open('E:\\Downloads\\manager_sales.json', 'r') as json_file:
#     python_file = json.load(json_file)
#     name = ''
#     summ = 0
#     for i in python_file:
#         mid = sum([j['price'] for j in i['cars']])
#         if mid > summ:
#             summ = mid
#             name = i['manager']['first_name'] + ' ' +  i['manager']['last_name']
# print(name, summ)


import json

with open('E:\\Downloads\\group_people.json', 'r') as file_json:
    data = json.load(file_json)
a = []
for i in data:
    a.append((i['manager']['first_name'], i['manager']['last_name'], sum(s['price'] for s in i['cars'])))

print(*sorted(a, key=lambda x: x[2], reverse=True)[0])