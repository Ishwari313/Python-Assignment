'''
Write a program which contains filter(),map() and reduce()
in it. Python application which contains one list of numbers.List contains
the numbers which are accepted from user. Filter should filter out all such numbers
which greater than or equal to 70 and less than or 
equal to 90. Map functiom will increase each number by 10.
reduce will retuen product of all that numbers.
'''

from functools import reduce

def main():
    lst=[]
    N=int(input("Enter how many no you want insert:"))

    for i in range(N):
        Num=int(input(f"Enter the Numbers {i+1}:"))
        lst.append(Num)

    print("Input list =",lst)

    Fdata=list(filter(lambda Num : Num >= 70 and Num <=90, lst))
    print("List After filter",Fdata)

    Mdata=list(map(lambda Num:Num + 10,Fdata))
    print("list after map=",Mdata)

    Rdata=reduce(lambda x,y:x*y,Mdata)
    print("Result after reduce =",Rdata)

if __name__=="__main__":
    main()