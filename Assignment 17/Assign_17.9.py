# Write a program which accept number from user and
# return number ofm digits in that number

def CountDigit(No):

    cnt=0
    
    while No !=0:
        No = No // 10
        cnt +=1
    
    return cnt


def main():

    Num = int(input("Enter the No: "))
    
    print("count od digits",CountDigit(Num))

if __name__ =="__main__":
    main()