# WRITE A LAMBDA FUNCTION WHICH ACCEPTS TWO NUMBERS AND RETURNS ADDITION

Add = lambda No1 ,No2 : No1+No2

def main():
    Val1=0
    Val2=0
    Ret=0

    Val1=int(input("Enter the First Number: "))
    Val2=int(input("Enter the Second Number "))

    Ret =(Add(Val1,Val2))
    print("The Addition is:",Ret)

if __name__ =="__main__":
    main()
