for i in range(-2, 6):
    print(i)
print("Hi")

for i in range(1, 6):
    print(i)
print()

for i in range(1, 6, 2):
    print(i)
print()

word = "My text"
for i in word:
    print(i)
print()
for i in word:
    if i == "t":
        print("Yes")
print()
count = 0
for i in word:
    if i == "t":
        count += 1
print("t:", count)
print()

i = 8
while i <= 24:
    print(i)
    i += 5
print()

# while True:
#   i *= 1000100010
#   print(i)

while True:
    print(i)
    if input() == "stop":
        break
print()

for i in range(1, 18):
    if i % 5 == 0:
        continue
    print(i)
print()

found = None
for i in "hello":
    if i == "l":
        found = True
        break
    else:
        found = False
print(found)
