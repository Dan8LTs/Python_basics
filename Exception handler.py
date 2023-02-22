x = 0
while x != 1:
    try:
        x = int(input("Enter the number: "))
        x += 5
        print(x)
        x = 1
    except ValueError:
        print("You entered not a number!")
    else:
        print("There were no mistakes")
    finally:
        print(str(x) + "\n")