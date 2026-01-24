# WRITW A LAMBDA FUNCTION USING FILTER() WHICH ACCEPS A LIST OF NUMBERS AND RETURNS ALIST OF EVEN NUMBERS

EvenNum = lambda No : (No % 2 == 0)

def main():
    numbers=[12,45,67,4,3,5,66,45,67,3,23,45,87,32,90,54,32,22,11]

    Fdata=list(filter(EvenNum,numbers))

    print("The Even Numbers are:",Fdata)


if __name__ =="__main__":
    main()
