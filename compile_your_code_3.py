import json
with open('E:\\Downloads\\group_people.json', 'r') as file_json:
    data = json.load(file_json)
lst = []
for i in data:
    count = 0
    for j in i['people']:
        if j['year'] > 1977 and j['gender'] == 'Female':
            count += 1
    lst.append((i['id_group'], count))
print(*sorted(lst, key=lambda x: x[1], reverse=True)[0])


-------------------------------------------------------------------------------------------------
import json
def get_young_ladies(group):
    return sum([1 for i in group['people'] if i['gender'] == 'Female' and i['year'] > 1977])
with open("group_people.json", "r") as file:
    dd = json.load(file)
best = max(dd, key=get_young_ladies)
print(best['id_group'], get_young_ladies(best))


-------------------------------------------------------------------------------------------------
import json
with open('group_people.json') as json_data:
    data = json.load(json_data)
lst = [0, 0]
for group in data:
    count = sum([person['gender'] == 'Female' and person['year'] > 1977 for person in group['people']])
    if lst[1] < count:
        lst = [group['id_group'], count]
print(*lst)


