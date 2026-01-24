# WRITE A LAMBDA FUNCTION USING FILTER() WHICH ACCEPTS A LIST OF NUMBERS AND RETURNS A LIST OF NUMBERS DIVISIBLE BY BOTH 3 AND 5

Div = lambda X :(X % 3==0) and(X % 5 ==0)

def main():

    Numbers=[12,15,30,45,36,78,98,90,41,34,54,67,80,30,60]
    Fdata=list(filter(Div, Numbers))
    print("The data after Filtering: ",Fdata)

if __name__ =="__main__":
    main()