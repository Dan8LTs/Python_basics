# Кортеж - это список, в котором нельзя изменить элементы, а также кортежи весят меньше
data = (4, 6, 7, 3, 6, True, 5.6, 'Hello')
# data[0] = 5 - невозможно
print(data[1:5])
print()

# количество определённых элементов
print(data.count(6))
# количество элементов в кортеже
print(len(data))
print(data)
print()

# один из вариантов создания кортежа
items = 5, 2, 634, True
print(items)
for item in items:
    print(item)

item = (5,)
print(item)

nums = [5, 5, 5]
# преобразование списка в кортеж
new_data = tuple(nums)
print(new_data)

# преобразование строки в кортеж
word = tuple('Programming')
print(word)