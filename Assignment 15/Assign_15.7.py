#WRITE A LAMBDA FUNCTION USINF FILTER() WHICH ACCEPTS A LIST OF STRINGS AND RETURNS A LIST OF STRINGS HAVING LENGTH GRATER THAN 5

Maxlen = lambda s: len(s)>5

def main():
    str=["Ishwari","Piyu","Purva","Shivam","Rudra","Bhakti","Vandana","Dnyaneshwar"]

    FData=list(filter(Maxlen,str))

    print("The Data Afte Filtering: ",FData)

if __name__ == "__main__":
    main()
