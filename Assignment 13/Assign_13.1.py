# WRITE A PROGRAM WHICH ACCEPTS LENGTH AND WIDTH OF RECTANGLE AND PRINTS AREA

def AreaofRec(L, W):
    Area= L *W
    print(Area)

def main():
    lenth=float(input("Enter the Lenghth: "))
    width=float(input("Enter the width: "))

    print("The Area of rectangle is :")
    AreaofRec(lenth,width)

if __name__ =="__main__":
    main()