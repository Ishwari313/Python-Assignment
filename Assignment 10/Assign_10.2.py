# Write a program whci accepts one number and prints sum of first N natural no
def SumNo(No):
    sum= No*(No+1)/2
    print(sum)

def main():
    No=int(input("Enter the No: "))
    SumNo(No)

if __name__ =="__main__":
    main()