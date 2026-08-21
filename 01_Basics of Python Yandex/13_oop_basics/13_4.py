class Programmer:

    def __init__(self, name, position="Junior"):
        self.name = name
        self.position = position
        self.worked = 0
        self.money = 0
        self.overrises = 0

    def work(self, time):
        grade = {
            "Junior": 10,
            "Middle": 15,
            "Senior": 20,
        }
        self.worked += time
        self.money += time * (grade[self.position] + self.overrises)

    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
        elif self.position == "Middle":
            self.position = "Senior"
        elif self.position == "Senior":
            self.overrises += 1

    def info(self):
        return f'{self.name} {self.worked}ч. {self.money}тгр.'

programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)


