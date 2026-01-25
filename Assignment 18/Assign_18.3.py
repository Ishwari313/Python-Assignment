# write a program which accept N numbers from user and store it into list. 
# Return min number frm that list


def MinNo(lst):
    Min =lst[0]
    for no in (lst):
        if no<Min:
            Min = no
    return Min
            
        
def main():
    N=int(input("Enter the No you want to store: "))
    lst=[]

    for i in range(N):
        Numbers=int(input(f"Enter the numbers {i+1}:"))
        lst.append(Numbers)

    ret= MinNo(lst)
    print("Max no is:" ,ret)
    
if __name__ =="__main__":
    main()
