def flatten_dict(d: dict) -> dict:
    dic1 = {}
    for k,v in d.items():
        if type(v) == dict:
            dic1[str(k) + '_' + str(flatten_dict(v).popitem()[0])] = flatten_dict(v).popitem()[1]
        elif type(v) == int:
            dic1[k] = v
    return dic1

def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }


nested = {'Geeks': {'for': {'for': 1, 'geeks': 4}}, 'for': {'geeks': {'Geeks': 3}}, 'geeks': {'Geeks': {'for': 7}}}

print({'Geeks_for_geeks': 4, 'for_geeks_Geeks': 3, 'geeks_Geeks_for': 7} ==
      {'Geeks_for_geeks': 4, 'for_geeks_Geeks': 3, 'geeks_Geeks_for': 7, 'Geeks_for_for': 1})
print(flatten_dict(nested))










# for k,v in nested.items():
#     if type(v) == dict:
#         for kk,vv in v.items():
#             print(kk,vv)
#         n[str(k) + '_' + str(kk)] = vv
#     else:
#         break
# print(n)

#print(flatten_dict(nested))

# {'Germany_berlin': 7,
#                          'Europe_italy_Rome': 3,
#                          'USA_washington': 1,
#                          'USA_New York': 4}