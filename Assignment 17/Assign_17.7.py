def DisplayPattern(No):

    for i in range(No):
        for j in range(1,No+1):
            print(j,end=" ")
        print()

def main():
    No=int(input("Enter The Number: "))

    DisplayPattern(No)
if __name__=="__main__":
    main()

'''
Enter The Number: 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

'''