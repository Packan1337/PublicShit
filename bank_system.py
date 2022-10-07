from faker import Faker

fake = Faker()
all_bank_users = []


# car class.
class Car:
    def __init__(self, car_brand: str, model: str, model_year: int, mileage: int):
        self.car_brand = car_brand
        self.model = model
        self.model_year = model_year
        self.mileage = mileage


# house class.
class House:
    def __init__(self, house_type: str, house_area: str, house_m2: int):
        self.house_type = house_type
        self.house_area = house_area
        self.house_m2 = house_m2

    @staticmethod
    def display_house(house_to_display):
        house = house_to_display
        return f"{house.house_m2}{house.house_type} in {house.house_area}"


# bank user class.
class BankUser:
    def __init__(self, first_name: str, last_name: str, bank_id: str, asset):
        self.user_assets = []

        self.first_name = first_name
        self.last_name = last_name
        self.bank_id = bank_id
        self.asset = asset

        self.user_assets.append(asset)

    # method to get name of car.
    @staticmethod
    def display_car(car_to_display):
        car = car_to_display
        return f"{car.car_brand} {car.model}"

    # function that displays a bank user and their BankID and assets.
    def display_bank_user(self):
        bank_user = self
        print(f"""
{bank_user.first_name} {bank_user.last_name}
BankID: {bank_user.bank_id}
Assets: {bank_user.display_car(bank_user.user_assets[0])}
""")


# create a new bank user.
def create_bank_user():
    global asset_to_add
    print("Want to add an asset with new user?")
    state = int(input("1. Yes, 2. No: "))

    if state == 1:
        state = int(input("1. Add car asset, 2. Add house asset: "))

        if state == 1:
            asset_to_add = Car(input("Manufacturer: "),
                               input("Model: "),
                               int(input("Model year: ")),
                               int(input("Milage: ")))
        elif state == 2:
            asset_to_add = House(input("House type: "),
                                 input("House area: "),
                                 int(input("House m2: ")))

    all_bank_users.append(BankUser(input("Enter first name: "), input("Enter last name: "), fake.swift(), asset_to_add))


def display_all_bank_users():
    for users in all_bank_users:
        print(f"""
{users.first_name} {users.last_name}
BankID: {users.bank_id}
""")

def generate_users():
    all_bank_users.append(BankUser(fake.first_name(), fake.last_name(), fake.swift(), Car("Mercedes-Benz", "S580", 2022, 5000)))

for _ in range(25):
    generate_users()


#create_bank_user()


display_all_bank_users()