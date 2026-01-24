# Write a lambda function which accepts two numbers and returns the max number

Max = lambda No1, No2 :No1 if (No1>No2) else No2

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    Value1 = int(input("Enter the First number: "))
    Value2 = int(input("Enter the Second Number : "))

    Ret=max(Value1,Value2)

    print("Maximum number is:",Ret)

if __name__ =="__main__":
    main()