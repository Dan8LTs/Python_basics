nums = [0, 5, 8, 81, 234, True, "Hi", 250.128, ["a", "b"]]
nums[0] = 4
print(nums)
# [-1] - the last element
print(nums[-1][1])

numbers = [6, 9, 7]
# numbers[3] = 100 - не имеет смысла
numbers.append(100)
# insert(индекс, значение) - поместить новый элемент со смещением остальных
numbers.insert(2, True)
# extend - добавить список в конец другого списка
numbers.extend([8, 9, 5])
print(numbers)
# True = 1
numbers.sort()
print(numbers)

# удалить элемент по индексу
numbers.pop(0)
# удалить конкретный элемент
numbers.remove(6)

# numbers.clear()

# количество элементов по значению
print(numbers.count(True))

# количество элементов
print(len(numbers))
print()

ns = [2, 4, 6, 3, True, False]
for el in ns:
    el *= 2
    print(el)

user_list = []
i = 0
while True:
    string = "Enter element #" + str(i + 1) + ":"
    userdata = input(string)
    if userdata == "stop":
        break
    else:
        user_list.append(int(userdata))
        i += 1
print(user_list)
