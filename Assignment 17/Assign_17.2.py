# write a program which accepts a number and prints the star with the same no of row and column

def PrintPattern(No):
    for i in range(No):
        for j in range(No):
            print("*",end=" ")
        print()
def main():

    No=int(input("Enter the No: "))
    PrintPattern(No)

if __name__=="__main__":
    main()



'''# OUTPUT #
Enter the No: 5
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''