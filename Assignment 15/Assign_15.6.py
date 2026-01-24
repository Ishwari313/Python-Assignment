# WRITE A LAMBDA FUNCTION USING REDUCE() WHICH ACCEPTS A LIST OF NUMBERS AND RETURNS THE MINIMUM ELEMENST

from functools import reduce
MinNo = lambda No1,No2 : No1 if(No1 < No2)else No2

def main():

    Numbers=[12,4,43,56,75,3,2,45,78,87]

    Rdata= reduce(MinNo,Numbers)

    print("The Data After reducing is",Rdata)

if __name__ =="__main__":
    main()