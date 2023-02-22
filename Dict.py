# {ключ, значение}
language = {5: 8}

# 2 способ: country = dict(code='RU', name='Russian', 'population'=144)
country = {'code': 'RU', 'name': 'Russian', 'population': 150}
# изменение элемента
# = country.update({'code': 'Rus'})
country['code'] = 'Rus'
# print(country['name'])

for key in country:
    print(key)
print()

for key, val in country.items():
    print(key, ":", val)
print()

# = country['name']
print(country.get('name'))
print(country)
# pop - удаление элемента по ключу
# popitem() - удаление последнего элемента
country.pop('name')
print(country)
print()

print(country.values())
print(country.keys())
print(country.items())
print()

country.clear()
print(country)

person = {
    'user1': {
        'first_name': 'Jenya',
        'last_name': 'Semenov',
        'age': 14
    },
    'user2': {
        'first_name': 'Nikita',
        'last_name': 'Shishov',
        'age': 15
    }
}

print(person['user2'].values())
