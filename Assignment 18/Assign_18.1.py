# write a program which accepts N numbers from user and store it into
# list. Return Addition of all elemnts from that list

def Addition(lst):
    sum = 0
    for num in lst:
        sum = sum + num
    return sum

def main():
    N =int(input("Enter a number you want to store:"))
    list=[]

    for i in range(N):
        Numbers=int(input(f"Enter the Numbers {i+1}: "))
        list.append(Numbers)

    Ret=Addition(list)
    print("Addition: ",Ret)
if __name__ =="__main__":
    main()