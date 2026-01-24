# WRITE A LAMBDA FUNCTION WHICH ACCEPTS ONE NUMBER AND RETURNS CUBE OF THAT NUMBER

Cube =lambda X: X*X*X

def main():
    X = int(input("Enter the Number: "))
    print(Cube(X))

if __name__ =="__main__":
    main()