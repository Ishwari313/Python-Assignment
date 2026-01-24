'''
Write a program which contains one function that accepts one number from user and returns true if number is divisible by 5 otherwise return false

'''

def Div(No):
    if No %5 ==0:
        print("True")
    else:
       print("False")

def main():

    No=int(input("Enter the No: "))

    Div(No)

if __name__=="__main__":
    main()