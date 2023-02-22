# This is a comment
# I am starting to learn Python
print("This is Python)")
print("Five is string: 5")
print("Five is number:", 5)
# sep replaces spaces
print("Five is number:", 5, "this is a text", 4, sep="(You can delete this space!)")
print()

print("Five is number:", 5, "this is a text", end="!")
print(" New line")
print()

# \n - new line; \" - " is string; \t - tab; \\ - \ is string
print("This book is \"Robinsone\n \t\t Crusoe\"\\")
print()

print(5 // 3)
print(5 / 3)
x = 5
x **= 2
print(x)
# Оператор	Название	    Значение
#     &     И   	        Устанавливает каждый бит в 1, если оба бита 1
#     |     Или	            Устанавливает каждый бит в 1, если один из двух битов 1
#     ^	    Только или	    Устанавливает каждый бит в 1, если только один из битов 1
#     ~	    Не	            Переставляет все биты
#    <<     Сдвиг влево	    Сдвигает влево на количество бит указанных справа
#    >>	    Сдвиг вправо	Сдвигает вправо на количество бит указанных справа

print(min(5, 7, -2, 55, 5, 5, 5))
print(max(5, 7, -2, 55, 5, 5, 5))
print(pow(5, 3))
print(round(5 / 3))
print()

input()
input("Enter your age:")