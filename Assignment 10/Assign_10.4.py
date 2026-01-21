# WRITE A PROGRAM WHICH ACCEPTS ONE NUMBER AND PRINTS ALL EVEN NUMEBRS TILL TAHT NUMBER


def PrintEven(No):
    for i in range(1, No+1):
        if i % 2==0:
            print(i)

def main():
    No = int(input("Enter the No: "))
    PrintEven(No)

if __name__=="__main__":
    main()
