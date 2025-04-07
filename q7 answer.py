class Car:
  def __init__(self, make, model, year):  #define class Car with 3 attributes
    self.make = make
    self.model = model
    self.year = year

  def describe_car(self):               #define describe car function to print Year Model Make
        print("This Car is " + self.year + " " + self.make + " " + self.model )

c1 = Car("Toyota", "Corolla", "2020")    #Task 2 Q1 Define instance of Car
c1.describe_car()                        #Task 2 Q2 Call describe car function