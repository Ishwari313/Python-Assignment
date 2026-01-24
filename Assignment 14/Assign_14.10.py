# WRITE A LAMBDA FUNCTION WHICH ACCEPTS THREE NUMBERS AND RETURNS LARGEST NUMBER

MaxInThree =lambda No1, No2, No3 : No1 if (No1 >= No2 and No1 >= No3) else (No2 if ( No2 >= No1 and No2 >=No3) else No3)

def main():
    Val1 = 0
    Val2 = 0
    Val3 = 0

    Ret = 0

    Val1 = int(input("Enter the Fisrt Number: "))
    Val2 = int(input("Enter the Second Number: "))
    Val3 = int(input("Enter the Third Number: "))

    Ret=(MaxInThree(Val1, Val2, Val3))

    print("The Largest Number is:",Ret)

if __name__ =="__main__":
    main()