# WRITE A LAMBDA FUNCTION USING REDUCE() WHICH ACCEPTS LIST OF NUMBERS AND RETURNS THE MAXIMUM NUMBERS

from functools import reduce

MaxNo = lambda No1,No2: No1 if (No1 > No2) else No2

def main():
    Numbers=[12,34,56,78,98,65,80]

    RData =reduce(MaxNo, Numbers)

    print("Data After Reducing:",RData)

if __name__ =="__main__":
    main()
