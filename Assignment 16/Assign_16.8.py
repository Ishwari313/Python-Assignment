'''
Write a program which accepts number from user and prints that number of
"*" on screen
'''
def Star(No):
    for i in range (No):
        print("*")

def main():

    No=int(input("Enter the Number: "))

    Star(No)

if __name__ =="__main__":
    main()
