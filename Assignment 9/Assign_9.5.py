def ChkDiv(No):
    if (No %3==0 and No% 5==0):
        print("Divisible by 3 and 5")

    else:
        print("Not Divisible")

def main():
    No= int(input("Enter the No you want to check: "))
    ChkDiv(No)

if __name__ == "__main__":
    main()