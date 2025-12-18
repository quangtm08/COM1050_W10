from animal import Animal

class Cat(Animal):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def sound(self):
        return "meow"


        