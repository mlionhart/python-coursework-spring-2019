# Module 8 - Programming Assignment 11 Problem 1

## Create a Car Class

Create a class named Car.

When the class is instantiated three instance variables are defined:

- _make
- _model
- _year

The constructor function should include the parameters make, model and year.

Six methods are to be created in the **Car** class:

- set_make(self,make)
- set_model(self,model)
- set_year(self,year)
- get_make(self)
- get_model(self)
- get_year(self)

Create a TestCar() function that

- Creates a list named **carLot**
- Add 5 Car objects to the list. Make up the makes, models and years for each of your cars.
- Create a loop that displays each cars properties for each car object in the list
- Create another loop that iterates through the list of cars and calls each of the three set methods to change the make, model and year of each car.
- Repeat the first loop to display the updated list.
- Use conditional execution ("if __name__ == "__main__":) to call the TestCar function