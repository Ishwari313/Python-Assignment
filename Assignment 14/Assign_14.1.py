# WRITE A LAMBDA FUNCTION WHICH ACCEPTS ONE NUMBER AND RETURNS SQUARE OF THAT NUMBER

Square =lambda X: X*X

def main():
    X = int(input("Enter the Number: "))
    print(Square(X))

if __name__ =="__main__":
    main()