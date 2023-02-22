word = "Danil-LTs"
# count - количество определённых элементов в списке
print(word.count('l'))
# upper - переход в верний регистр
print(word.upper())
# isupper - проверяет в верхнем ли регистре строка
print(word.isupper())
# find(строка) - находит индекс строки в строке
print(word.find("LT"))
# split - создаёт список из строк, созданых в результате разделения строки по элементу
words = word.split('-')
print(words)
# capitalize - приводит строку к виду с первым символом в верхнем регистре, а остальными - в нижнем
print(word.capitalize())

for i in range(len(words)):
    words[i] = words[i].capitalize()
print(words)

# делим и выводим элементы списка через запятую
result = ", ".join(words)
print(result)
print()

text = "Computer"
# [индекс нач. эл, индекс кон. эл., шаг] - деление списка или строки(индекс конечного элемента не включается)
print(text[3:-2:1])

lis = [3, 65, 4, "text", text, 3.56]
print(lis[4][:-2])
print(lis[::-1])
