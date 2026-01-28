'''
Write a python program to implement a class named Numbers 
with the following specification
:>The class should contain one instance varibale
    :>value
:>define a constructor(__init__) that accepts a number from the user and initializes value
:>Implement the following instance methods:
    :>ChkPrime()-returns True if the number is prime otherwise returns False
    :>ChkPerfect()-returns True if the number is perfect, otherwise returns false
    :>Factors()-displays all factors of the numbers
    :>SumFactors()-returns the sum of all the factors

:>Create multiple objects and call all the methods
'''

class Numbers:
    def __init__(self):
        self.value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, int(self.value**0.5) + 1):
            if self.value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        sum_factors = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                sum_factors += i
        return sum_factors == self.value

    def Factors(self):
        print(f"Factors of {self.value}:", end=" ")
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum_factors = 0
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                sum_factors += i
        return sum_factors


print("\nObject 1:")
obj1 = Numbers()
print("Prime?:", obj1.ChkPrime())
print("Perfect?:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors:", obj1.SumFactors())

print("\nObject 2:")
obj2 = Numbers()
print("Prime?:", obj2.ChkPrime())
print("Perfect?:", obj2.ChkPerfect())
obj2.Factors()
print("Sum of Factors:", obj2.SumFactors())