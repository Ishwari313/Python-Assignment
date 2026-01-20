'''Write a program which accepts one number and prints cube of that number'''

def Cube(No):
    Cube= No * No *No
    print("The Square of the no is:",Cube)

def main():
    No= int(input("Enter the No :"))
    Cube(No)

if __name__=="__main__":
    main()
