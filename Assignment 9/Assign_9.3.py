'''Write a program which accepts one number and prints square of that number'''

def Square(No):
    Square= No * No
    print("The Square of the no is:",Square)

def main():
    No= int(input("Enter the No :"))
    Square(No)

if __name__=="__main__":
    main()
