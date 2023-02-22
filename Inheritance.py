# множественное наследование существует
class Building:
    # __ инкапсуляция
    __year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year:", self.year, ".City:", self.city)


# наследование
class School(Building):
    pupil = 0

    def __init__(self, pupil, year, city):
        # обращение к родительскому классу
        super(School, self).__init__(year, city)
        self.pupil = pupil

    def get_info(self):
        super().get_info()
        print("Pupil:", self.pupil)


school = School(1000, 2021, 'Moscow')
school.get_info()
house = Building(2021, 'Cheboksary')
shop = Building(2021, 'Moscow')
