'''Write a program which contains one function chkgreater() that accepts two numbers and prints the greater number'''

def ChkGreater(No1, No2):
    
    if No1 < No2:
        print(No2," is grater",)
    else:
        print(No1,"It is greater")


def main():
    No1 = int(input("Enter the first no:"))
    No2 = int(input("Enter the second no:"))

    ChkGreater(No1 , No2)

if __name__== "__main__":
    main()