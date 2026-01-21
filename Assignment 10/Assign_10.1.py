# Write a program which accepts one number and prints multiplication table of that number

def MultiNo(No):
    for i in range(1,11):
        result = No *i
        print(result)

def main():
    No=int(input("Enter the No to Multiply: "))
    MultiNo(No)

if __name__ == "__main__":
    main()