'''
Write a program which accepts N numbers from user and store it into list 
Accept one another number and return frequency of that number
from list
'''
def Freq(lst, No):
    count =0
    for i in lst:
        if i ==No:
            count +=1
    return count

def main():
    N=int(input("Enter how many number you want to store: "))
    lst=[]

    for i in range(N):
        num=int(input(f"Enter Numbes: {i+1}"))
        lst.append(num)

    value=int(input("Enter number to find Freq:"))

    ret= Freq(lst,value)
    print("Frequency:",ret)

if __name__ =="__main__":
    main()