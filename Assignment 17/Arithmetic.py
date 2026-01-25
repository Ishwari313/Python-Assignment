'''
Create on module named as Arithmetic which contains 4 functions
Add() for addition, Sub() for subbtraction,mult()
for multiplication and Div() for division. All functions accepts
twwo paramenters as number and perform the operation.
Write on python program which call all the functions from
Arithemetic module by accepting the parameters from user
'''

print("Inside Module:",__name__)

def Add(No1,No2):
    Ans=0
    Ans = No1 +No2
    return Ans

def Sub(No1,No2):
    Ans=0
    Ans = No1 - No2
    return Ans

def Mult(No1 ,No2):
    Ans=0
    Ans = No1 * No2
    return Ans

def Div(No1,No2):
    Ans=0
    Ans = No1 // No2
    return Ans

