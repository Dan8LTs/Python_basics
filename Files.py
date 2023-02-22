# w - write удаление и добавление информации
file = open('data/text.txt', 'w')
file.write('Python\n')
# \n - new line
file.write('Programming\n\n')

# a - append добавление к текущему содержимому
file = open('data/text.txt', 'a')
file.write('Python')
file.write('Programming')
file.close()

data = input("Enter text: ")
file2 = open('data/text2.txt', 'a')
file2.write(data + "\n")
file2.close()

file2 = open('data/text2.txt', 'r')
print(file2.read(8))
file2.close()
