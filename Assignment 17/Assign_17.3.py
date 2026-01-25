# Write a program which accept one number from user and return its factorial

def Factorial(N):
    if N<=1:
        return 1
    else:
        return N* Factorial(N-1)
    
def main():
    No = int(input("Enter the No:"))
    if No<0:
        print("fact not defined")
    else:
        fact=Factorial(No)

    print(f"The factorial of no is: {fact}")

if __name__ =="__main__":
    main()
