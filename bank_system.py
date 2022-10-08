import random
from faker import Faker

# global variables.
m2 = "m" + "\u00B2"
fake = Faker()
all_bank_users = []
# used for fake user generator, cba put it in separate file.
dummy_cars = ["Mercedes-Benz S580",
              "Mercedes-Benz C300e",
              "Mercedes-AMG GTR",
              "BMW M8",
              "BMW 330e",
              "BMW X5M",
              "Audi S8",
              "Audi RS3",
              "Audi TT",
              "Porsche 911 GT3",
              "Porsche Macan S",
              "Porsche Taycan Turbo S",
              "Volkswagen ID.4",
              "Volkswagen Golf R",
              "Volvo XC60 T8",
              "Volvo S90 T6"]

dummy_houses = ["Villa", "Appartment", "Townhome", "Condo"]
dummy_areas = ["Malaga", "Berlin", "Tokyo", "Stockholm", "Oslo", "Barcelona", "New York"]


# car class.
class Car:
    def __init__(self, car: str, model_year: int, mileage: int):
        self.car = car
        self.model_year = model_year
        self.mileage = mileage


# house class.
class House:
    def __init__(self, house_type: str, house_area: str, house_m2: int):
        self.house_type = house_type
        self.house_area = house_area
        self.house_m2 = house_m2


# bank user class.
class BankUser:
    def __init__(self, first_name: str, last_name: str, bank_id: str, car=None, house=None):
        self.user_cars = []
        self.user_houses = []

        self.first_name = first_name
        self.last_name = last_name
        self.bank_id = bank_id
        self.car = car
        self.house = house

        self.user_cars.append(car)
        self.user_houses.append(house)

    # method to get name of car.
    @staticmethod
    def display_car(car_to_display):
        car = car_to_display
        return f"{car.car}"

    @staticmethod
    def display_house(house_to_display):
        house = house_to_display
        return f"{house.house_m2}{m2} {house.house_type} in {house.house_area}"

    # method that displays a bank user and their BankID and assets.
    def display_bank_user(self):
        bank_user = self

        # prints users with both houses and cars.
        if bank_user.house is not None and bank_user.car is not None:
            print(f"""
{bank_user.first_name} {bank_user.last_name}
BankID: {bank_user.bank_id}
Assets
Cars: {bank_user.display_car(bank_user.user_cars[0])}
House(s): {bank_user.display_house(bank_user.user_houses[0])}
""")

        # prints users with only cars, not houses.
        elif bank_user.house is None and bank_user.car is not None:
            print(f"""
{bank_user.first_name} {bank_user.last_name}
BankID: {bank_user.bank_id}
Assets
Cars: {bank_user.display_car(bank_user.user_cars[0])}
""")

        # prints users with only cars, not houses.
        elif bank_user.house is not None and bank_user.car is None:
            print(f"""
{bank_user.first_name} {bank_user.last_name}
BankID: {bank_user.bank_id}
Assets
House(s): {bank_user.display_house(bank_user.user_houses[0])}
""")


# create a new bank user.
def create_bank_user():
    global asset_to_add
    print("Want to add an asset with new user?")
    state = int(input("1. Yes, 2. No: "))

    # select asset to add.
    if state == 1:
        state = int(input("1. Add car asset, 2. Add house asset: "))

        # car option.
        if state == 1:
            asset_to_add = Car(input("Car: "),
                               int(input("Model year: ")),
                               int(input("Milage: ")))

        # house option.
        elif state == 2:
            asset_to_add = House(input("House type: "),
                                 input("House area: "),
                                 int(input("House m2: ")))

    # obligatory user input data.
    all_bank_users.append(BankUser(input("Enter first name: "), input("Enter last name: "), fake.swift(), asset_to_add))


# function that displays all bank users.
def display_all_bank_users():
    for users in all_bank_users:
        BankUser.display_bank_user(users)


# function that generates a fake user for testing purposes.
def generate_fake_users():
    # variable that decides if fake user's assets
    random_pick = random.randint(1, 3)

    if random_pick == 1:
        # generates user with car.
        all_bank_users.append(BankUser(fake.first_name(),
                                       fake.last_name(),
                                       fake.swift(),
                                       Car(random.choice(dummy_cars),
                                           2022,
                                           5000)))

    elif random_pick == 2:
        # generates user with house.
        all_bank_users.append(BankUser(fake.first_name(),
                                       fake.last_name(),
                                       fake.swift(),
                                       None,
                                       House(random.choice(dummy_houses),
                                             random.choice(dummy_areas),
                                             random.randrange(30, 100))))

    elif random_pick == 3:
        # generates user with car and house.
        all_bank_users.append(BankUser(fake.first_name(),
                                       fake.last_name(),
                                       fake.swift(),
                                       Car(random.choice(dummy_cars),
                                           2022,
                                           5000),
                                       House(random.choice(dummy_houses),
                                             random.choice(dummy_areas),
                                             random.randrange(30, 100))))


# generate multiple fake users.
for _ in range(100000):
    generate_fake_users()


display_all_bank_users()
