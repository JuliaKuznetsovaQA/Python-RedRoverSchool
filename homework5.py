class Animal:
    country = 'USA'

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self, word):
        return f'{self.name} says {word}'

    def how_old(self):
        return f'{self.name} is {self.age} years old'

    def move(self):
        return f'{self.name} can walk'

    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country
        print(cls.country)

    @staticmethod
    def is_adult(age):
        return age > 18


class Cat(Animal):
    def __init__(self, name, age, color, breed, cost):
        super().__init__(name, age, color)
        self.breed = breed
        self.__cost = cost

    def move(self):
        return f'Cat {self.name} can jump and run'

    def get_cost(self):
        return f'{self.name} costs {self.__cost} EUR'

    def set_cost(self, new_cost):
        self.__cost = new_cost
        return f' New cost of {self.name} is {self.__cost}'


class Fish(Animal):
    def __init__(self, name, age, color, breed, cost):
        super().__init__(name, age, color)
        self.breed = breed
        self.__cost = cost

    def move(self):
        return f'Fish {self.name} can swim'

    def get_cost(self):
        return f'{self.name} costs {self.__cost} EUR'

    def set_cost(self, new_cost):
        self.__cost = new_cost

print(type(a))
pushok = Cat('Pushok', 12, 'black', 'trivial', 8000)
print(pushok.move())
print(pushok.__dict__)
print(pushok.speak('miau'))
print(pushok.get_cost())
pushok.set_cost(9000)
print(pushok.get_cost())
print()

golden_fish = Fish('Anita', 1, 'golden', 'golden fish', 1152)
print(golden_fish.how_old(), golden_fish.move())
print(golden_fish.__dict__)
print(golden_fish.get_cost())
golden_fish.set_cost(1200)
print(golden_fish.get_cost())
print()

murka = Cat('Murka', 7, 'white', 'persian', 2000)
print(murka.get_cost())
print(murka.move(), murka.speak('mau'))
print(murka.__dict__)

dog = Animal('Sharik', 6, 'grey')
print(dog.speak('gav'), dog.how_old())
dog.change_country('Russia')
print(dog.country)
print(dog.__dict__)
print(murka.country)
print(pushok.country)
print(pushok.is_adult(3))
print(dog.move())
