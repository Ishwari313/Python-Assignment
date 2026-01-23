# WRITE A PROGRAM WHICH ACCEPTS ONE NUMBER AND PRINTS ITS FACTOR
def Factors(No):
    cnt=1
    while cnt<=No:
        if No % cnt==0:
            print (cnt)
        cnt +=1

def  main():
    Num =0
    Num = int(input("Enter the no: "))
    print("The factors are ")
    Factors(Num)
if __name__ =="__main__":
    main()