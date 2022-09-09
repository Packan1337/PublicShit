# Defining car class
class Car:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    def __str__(self):
        return "{} {} {}".format(self._brand, self._model, self._year)
# Making the car object
def make_car():
    user_car = {}
    state = int(input("Would you like to make a car?\n\n1. Yes\n2. No\n\n"))

    if state == 1:
        print("Making a new car!\n")
        user_car["brand"] = input("Which brand is it?: ")
        user_car["model"] = input("Which model is it?: ")
        user_car["year"] = input("Which year is it?: ")
        return user_car

# Printing the car
car = Car(**make_car())
print(car)
