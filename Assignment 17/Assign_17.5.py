# WRITE A PROGRAM WHICH ACCEPTS ONE NUMBER AND CHECKS WHETHER IT IS PRIME OR NOT

def CheckPrime(No):
    if No < 0:
        No = -No
    
    if No < 2:
        return False
    
    flag = True

    cnt=2

    while cnt <=(No//2):
        if (No % cnt) == 0:
            flag =False
            break
        cnt +=1
    return flag


def main():
    No = int(input("Enter the No: "))
    Ret = CheckPrime(No)
    
    if Ret:
        print(f"{No} is prime no")

    else:
        print(f"{No} Not a prime no ")
    

if __name__ =="__main__":
    main()