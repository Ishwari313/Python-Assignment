# WRITE A LAMBDA FUNCTION WHICH ACCEPTS ONE NUMBER AND ETURNS TRUE IF NUMBER IS EVEN OTHERWISW FALSE

EvenNo = lambda No:True if(No % 2==0) else False

def main():
    val=0
    Ret =0

    val = int(input("Enter the Number: "))
    Ret= EvenNo(val)
    print(EvenNo(Ret))

if __name__ =="__main__":
    main()