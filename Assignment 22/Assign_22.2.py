# Write a python program to implement a class named circle with the following requirements:
# The class should contain three intance varibles:Radius,area and Circumference
#The class should contain one class variable named pi. initialized to 3.14
# Define a constructor (__init__) that initializes all instance varibles to 0.0
# Implement the follwing instance methosds
# 1>Accept()- Accepts the radius of the circle from the user
# 2> CalculateArea()-calculates the area of the circle and stores it in the Area variable
# 3> CalculateCircumference()- calculates the circumference of the circle and stores it in the circumference variable
# Display()- displays the value of Radius ,Area and Circumference

# Create multiple objects of the circle class and invl-oke all the instance methods for each object


class circle:
    pi=3.14

    def __init__(self):
        self.radius=0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.radius = float(input("Enter Radius:"))

    def CalculateArea(self):
        self.Area = circle.pi *self.radius *self.radius

    def CalculateCircumference(self):
        self.Circumference =2*circle.pi*self.radius

    def Display(self):
        print("Radius:",self.radius)
        print("Area:",self.Area)
        print("Circumference:",self.Circumference)

obj1=circle()
obj2=circle()

print("Circle 1:")
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()


print("Circle 2:")
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()

