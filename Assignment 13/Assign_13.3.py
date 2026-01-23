# WRITE A PROGRAM WHICH ACCEPTS ONE NUMBER AND CHECKS WHETHER IT IS PERFECT NUMBER OR NOT

def perfectNo(No):

    sum=0
    cnt=1
    while(cnt < No):
        if No % cnt==0:
            sum=sum +cnt
        cnt =cnt+1

    if sum == No:
        print("Perfect Number")
    else:
        print("Not a perfect No")


def main():
    Num=int(input("Enter the no:"))
    perfectNo(Num)

if __name__ == "__main__":
    main()