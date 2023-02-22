if 5 == 5:
    print("Yes")
    print("Great")

isHappy = True
if isHappy:
    print("User is happy!")
if not isHappy:
    print("User is not happy.")
print()

user_age = int(input("Enter your age:"))
if user_age >= 18:
    print("You are an adult!")
    # and/or
    if user_age >= 60 and isHappy:
        print("You are a happy retiree!")
elif user_age > 10:
    print("You are a teenager!")
else:
    print("You are a child.")
print()

data = input()
# if data == "eight":
#	number = 8
# else:
#	number = 0
number = 8 if data == "eight" else 0
print(number)
