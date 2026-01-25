from MarvellousNum import ChkPrime

def ListPrime(lst):
    sum = 0
    for no in lst:
        if ChkPrime(no):
            sum +=no
    return sum

def main():
    N=int(input("Enter how many numbers you want to store: "))
    lst=[]

    for i in range(N):
        num=int(input(f"Enter Number {i+1}:"))
        lst.append(num)

    result=ListPrime(lst)
    print("Addition:",result)

if __name__ =="__main__":
    main()