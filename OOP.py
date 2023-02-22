class Cat:
    name = None
    age = None
    isHappy = None

    # конструктор
    # isHappy = None значение по умолчанию
    def __init__(self, name, age, isHappy=None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    # можно передавать методы в конструктор

    # self - разрешение на взаимодействие c полями класса
    def get_data(self):
        print(self.name, "age:", self.age)


cat1 = Cat("Persik", 2, True)

cat2 = Cat("Mersi", 4)

print(cat1.name, cat1.age)
cat2.get_data()
