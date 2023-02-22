# Множество - это список, где нет повторяющихся элементов и они расположены в случайном порядке.
# data = set('Programming')
# {значение, значение}
data = {6, 7, 4, 5, 5}
print(data)

data.add(42)
# добавление элементов
data.update(['55', True, 8])
# удалить элемент по значению
data.remove(True)
# удалить первый элемент
data.pop()
print(data)

# очистить множество
data.clear()
print(data)

nums = [6, 8, 34, 5, 64]
# set - поместить элементы списка в множество
data = set(nums)
print(data)

data.clear()
# объединение кортежа и множества
data = frozenset([5, 1, 5, 6, 9, 8, 32, False])
# data.add() - запрещено
print(data)
