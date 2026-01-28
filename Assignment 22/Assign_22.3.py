'''
# Write a python program to implement a class named Arithmetic with the follwing Characteristic
:>The class should contain two instance variables: Value1 and Value2
:>Define a constructor (__init__) that initializes all instance variable to 0
:>Implement the following instance methods:
    :>Accept()-accepts value for value1 and value2 from the user
    :>Addition()-return the addition of value1 and value2
    :>Subtraction()-returns the subtraction of value1 and value2
    :>Multiplication()-returns the multiplication of value 1 and value2
    :>Division()-returns the division of value1 and value2 (handle division by zero properly)

Create multiple objects of the Arithmetic class and invoke all the instance methods
'''

class Arithmetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    
    def Accept(self):
        self.value1=int(input("Enter the first value:"))
        self.value2= int(input("Enter the Second value:"))

    def Addition(self):
        return self.value1+self.value2
    
    def Subtraction(self):
        return self.value1 - self.value2
    
    def Multiplication(self):
        return self.value1 * self.value2
    
    def Division(self):
        try:
            return self.value1 /self.value2
        
        except ZeroDivisionError:
            return "Cannot divide by zero"
        
obj1 = Arithmetic()
obj2 = Arithmetic()

print("Object 1:")
obj1.Accept()
print("Addition is:",obj1.Addition())
print("Subtraction is",obj1.Subtraction())
print("Multiplication is:",obj1.Multiplication())
print("Division is:",obj1.Division())

print("Object 2:")
obj2.Accept()
print("Addition is:",obj2.Addition())
print("Subtraction is",obj2.Subtraction())
print("Multiplication is:",obj2.Multiplication())
print("Division is:",obj2.Division())