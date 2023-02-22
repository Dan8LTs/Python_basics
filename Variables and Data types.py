number = 5
# del number - delete variable
print(number)
number = 7
print(number)
print()

digit = 4.231245  # float
print(number + digit)
word = "Result:"  # string
print(word, digit)
print()

boolvar = True  # bool
print(boolvar)

# str(var) - convert to string
# int(var) - convert to int
print(word + str(int(digit) + number))
print(int(4.5678))
print(int(4.9999))
print()

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Result+:", num1 + num2)
print("Result-:", num1 - num2)
print("Result*:", num1 * num2)
print("Result**:", num1 ** num2)
print("Result/:", num1 / num2)
print("Result//:", num1 // num2)
print("Result%:", num1 % num2)
num1 += num2
print("Result+=:", num1)
print()

word = "Hi!"
print(word * 2)

# True = 1; False = 0;
word = True
print(word * 2)
