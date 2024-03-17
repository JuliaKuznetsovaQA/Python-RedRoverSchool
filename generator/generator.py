import random

from data.data import User
from faker import Faker

faker_en = Faker("En")
Faker.seed()


def generated_user():
    yield User(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        full_name=generated_name(),
        address=faker_en.address(),
        # phone_number=faker_en.phone_number()
        phone_number=generated_phone_number()
    )


def generated_name():
    female = faker_en.name_female()
    male = faker_en.name_male()
    return random.choice([male, female])


def generated_phone_number():
    number = "+995" + "".join([str(random.randint(0, 9)) for _ in range(7)])
    return number


a = next(generated_user())
print(a.first_name)
print(a.last_name)
print(a.full_name)
print(a.address)
print(a.phone_number)