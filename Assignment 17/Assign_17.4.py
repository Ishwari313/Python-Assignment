# Write a program which accept one number from user and return addition ot its factor

def AdditionFactors(No):
    cnt = 1
    sum = 0

    while cnt < No:
        if No % cnt == 0:
            print(cnt)
            sum = sum + cnt
        cnt += 1

    print("Addition of factors is:", sum)

def main():
    No = int(input("Enter the Number: "))
    AdditionFactors(No)

if __name__ == "__main__":
    main()
