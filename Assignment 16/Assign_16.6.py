'''
Write a program which accepts number from user and check whether
that number is positive or negative or zero
'''
def Chkno(No):
    if No>0:
        print("Positive Number")
    elif No<0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    value=0

    value=int(input("Enter the Number: "))
    Chkno(value)

if __name__ =="__main__":
    main()
