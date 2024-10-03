dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)

print(dict2['a'])
print(dict2['a'] is dict1['a'])