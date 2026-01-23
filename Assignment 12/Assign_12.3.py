# WRITE A PROGRAM WHICH ACCEPTS TWO NUMBERS AND PRINTS ADDITION ,SUBTRACTION,MUTIPLICATIONAND DIVISON

def Operation(Num1,Num2):
    Add=Num1 +Num2
    Sub =Num1 - Num2
    MUlti= Num1* Num2
    Div= Num1// Num2

    print("Addition:",Add)
    print("Subtraction:",Sub)
    print("Multiplicaton:",MUlti)
    print("Division:",Div)

def main():
    Num1=int(input("Enter the First No: "))
    Num2= int(input("Enter the Second no: "))

    print("Operations are")
    Operation(Num1,Num2)

if __name__ =="__main__":
    main()