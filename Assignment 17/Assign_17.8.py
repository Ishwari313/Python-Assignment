def DisplayPattern(No):
    for i in range(1, No + 1):       
        for j in range(1, i + 1):    
            print(j, end=" ")
        print()

def main():
    No = int(input("Enter the Number: "))
    DisplayPattern(No)

if __name__ == "__main__":
    main()


'''

Enter the Number: 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''