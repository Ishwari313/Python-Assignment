'''
Write a program which contains one lambda function
 which accepts two parameters and returrn its multiplication
'''
Multi =lambda No1,No2:No1*No2

def main():
    value1=0
    value2=0

    value1=int(input("Enter first Number: "))
    value2=int(input("Enter second Number: "))

    ret=Multi(value1,value2)
    print("Multiplicaton:",ret)

if __name__ =="__main__":
    main()