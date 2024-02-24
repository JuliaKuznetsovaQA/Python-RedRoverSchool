"""5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
    нужно использовать методы get и set"""


class Person:
    country = 'USA'

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        return f'{self.fname}.{self.lname}@gmail.com'

    def hello(self):
        return f'{self.fname} {self.lname} says hello!'

    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country

class Programmer(Person):
    def __init__(self, fname, lname, language, job_tytle):
        super().__init__(fname, lname)
        self.language = language
        self.job_tytle = job_tytle

    def coding(self):
        return f'I\'m coding with {self.language}'


class Tester(Person):
    def __init__(self, fname, lname, framework, job_tytle):
        super().__init__(fname, lname)
        self.framework = framework
        self.job_tytle = job_tytle

    def testing(self):
        return f'I\'m testing with {self.framework}'


person_1 = Person('Oleg', 'Kuznetsov')

# print(person_1.fname)
# print(person_1.lname)
# print(person_1.hello())

tester_1 = Tester('Julia', 'Kuznetsova', 'pytest', 'Senior QA Engineer')
print(tester_1.fname, tester_1.lname, tester_1.hello(), tester_1.job_tytle, tester_1.testing())


class Developer(Person):
    def __init__(self, fname, lname, language, job_tytle, company, salary):
        super().__init__(fname, lname)
        self.language = language
        self._job_tytle = job_tytle
        self.company = company
        self.__salary = salary

    def coding(self):
        return f'I\'m coding with {self.language}'

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary


dev_1 = Developer('Dasha', 'Lukyanova', 'Java', 'Senior BE developer', 'PSB', 10000)
print(dev_1.fname, dev_1.lname, dev_1.hello(), dev_1.coding())
print(f'{dev_1.fname} {dev_1.lname} is working as {dev_1._job_tytle} at {dev_1.company}')
print(dev_1.__dict__)
dev_1.set_salary(300000)
print(dev_1.get_salary())
print(dev_1.__dict__)
# person_1.fname = 'Maxim'
# print(person_1.fname)
# print(person_1.__dict__)
print(dev_1.country)
print(dev_1.email)
dev_1.change_country('Russia')
print(dev_1.country)
dev_1.fname = 'Darya'
print(dev_1.fname, dev_1.email)
