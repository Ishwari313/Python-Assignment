# Write a program which accepts one number and prints factorial of that number
def Factorial(N):
    fact=(N)*(N-1)*(N-2)
    print("The Factorial of No is:",fact)
    
def main():
    No=int(input("Enter the No:"))
    Factorial(No)

if __name__ =="__main__":
    main()

