'''
Write a program  which contains filter(), map(),reduce() in it.
Python application which contains one list of numbers .list contains
the numbers which are accepted from user.filter should filter out all
such numbers which are even. map functon will calculate its square.
reduce will return addition of all that numbers
'''
from functools import reduce
def main():
    lst=[]
    N=int(input("Enter how many no you wnat to store: "))

    for i in range(N):
        Num=int(input(f"Enter the Number {i+1}:"))
        lst.append(Num)

    print("Input list = ",lst)

    Fdata=list(filter(lambda Num:(Num %2==0),lst))
    print("List after filter = ",Fdata)

    Mdata=list(map(lambda Num : Num * Num,Fdata))
    print("List after map =",Mdata)

    Rdata=reduce(lambda num1,num2:num1+ num2,Mdata)
    print("Output of reduce =",Rdata)

if __name__=="__main__":
    main()