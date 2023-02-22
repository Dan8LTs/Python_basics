# FileNotFoundError
# file = open("text.txt", "r")
# file.read()
# file.close()

# не закрывается
try:
    file = open("text.txt", "r")
    file.read()
    file.close()
except FileNotFoundError:
    print("File is not found")
#	file.close()

# name 'file' is not defined
# finally:
#	file.close()

try:
    with open("text.txt", "r", encoding="utf-8") as file:
        file.read()
except FileNotFoundError:
    print("File is not found")
