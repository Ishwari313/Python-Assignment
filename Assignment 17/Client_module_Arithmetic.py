import Arithmetic

def main():

    No1=int(input("Enter First No: "))
    No2=int(input("Enter Second Number: "))

    print("Addition is:",Arithmetic.Add(No1,No2))
    print("Subtraction is:",Arithmetic.Sub(No1,No2))
    print("Multiplication is:",Arithmetic.Mult(No1,No2))
    print("Division is:",Arithmetic.Div(No1,No2))

if __name__=="__main__":
    main()