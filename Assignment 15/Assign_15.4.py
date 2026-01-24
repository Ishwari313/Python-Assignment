# WRITE A LAMBDA FUNCTION USING REDUCE() WHICH ACCEPTS LIST OF NUMBERS AND RETURN THE ADDITION OF ALL ELEMENTS

from functools import reduce
Add = lambda A, B :A +B

def main():

    numbers=[1,2,3,4,5,6,7,8,9,10]

    RData = reduce(Add,numbers)
             
    print("Data after reduce is :",RData)

if __name__ =="__main__":
    main()