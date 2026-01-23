#WRITE A PROGRAM WHICH ACCEPTS ONE NUMBER AND PRINTS THAT MANY NUMBERS STARTIONF FROM 1

def print1toN(No):
    if No<0:
        return
    
    for i in range(1,No+1):
        print(i)

def main():
    No = int(input("Enter the Number: "))
    print("The No From Starting are:")
    print1toN(No)

if __name__=="__main__":
    main()

