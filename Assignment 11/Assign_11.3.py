# WRITE A PROGRAM WHICH ACCEPTS ONE NUMBER AND PRINTS SUM OF DIGITS 

def SumofDigits(No):
    total=0

    if No ==1:
        return 1
    
    while No !=0:
        Digits = No % 10
        total +=Digits
        No = No // 10


    return total


        
def main():
    Num=int(input("Enter the No:"))
    print("The Sum of Digit is",SumofDigits(Num))

if __name__ =="__main__":
    main()