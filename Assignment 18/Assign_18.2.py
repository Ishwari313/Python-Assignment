# write a program which accept N numbers from user and store it into list. Return maximum number frm that list

def MaxNo(lst):
    Max =lst[0]
    for no in (lst):
        if no>Max:
            Max = no
    return Max
            
        
def main():
    N=int(input("Enter the No you want to store: "))
    lst=[]

    for i in range(N):
        Numbers=int(input(f"Enter the numbers {i+1}:"))
        lst.append(Numbers)

    ret= MaxNo(lst)
    print("Max no is:" ,ret)
    
if __name__ =="__main__":
    main()
