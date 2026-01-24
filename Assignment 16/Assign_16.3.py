'''
Write a program which contains one function named as Add()
whcih accepts two numbers  from the user and return addition of that two numbers
'''
def Add(Num1,Num2):
    Ans= Num1 + Num2
    return Ans


def main():

    value1=int(input("Enter First Number: "))
    value2=int(input("Enter Second Number:"))

    Ret=Add(value1,value2)
    print("The Addition is:",Ret)

if __name__ =="__main__":
    main()
