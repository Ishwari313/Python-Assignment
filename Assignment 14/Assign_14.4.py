# WRITE A LAMBDA FUNCTION WHICH ACCEPTS TWO NUMBERS AND RETURNS MINIMUM NUMBER

Min = lambda No1, No2 : No1 if (No1<No2) else No2

def main():
    Value1 =0
    Value2 = 0
    Ret = 0

    Value1 = int(input("Enter the first No: "))
    Value2 = int(input("ENter the Second Number: "))

    Ret= Min(Value1,Value2)

    print("The Minimum no is",Ret)

if __name__ =="__main__":
    main()
