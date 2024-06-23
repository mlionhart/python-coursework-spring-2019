# Module 8
#   Programming Assignment 11
#     Prob-1.py
# Mike Hart


class Car(object):
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_year(self, year):
        self._year = year

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def Car_print(self):
        print('Make: ' + self._make, end="\t\t")
        print('Model: ' + self._model, end="\t\t")
        print('Year: ' + str(self._year), end="\t\t")


def TestCar():
    car1 = Car('Ford', 'Explorer', 1999)
    car2 = Car('Honda', 'Accord', 1993)
    car3 = Car('Toyota', 'Camry', 2004)
    car4 = Car('Nissan', 'Sentra', 2008)
    car5 = Car('Ford', 'Mustang', 1964)
    carLot = (car1, car2, car3, car4, car5)
    for item in range(5):
        carLot[item].Car_print()
        print()
    for item in range(5):
        carLot[item].set_make(input("What is the car's make? "))
        carLot[item].set_model(input("What is the car model? "))
        carLot[item].set_year(input("What is the year of the car? "))
    for item in range(5):
        carLot[item].Car_print()
        print()

if __name__ == "__main__": 
    TestCar()
