# WRITE A PROGRAM WHICH ACCEPTS RADIUS OF CIRCLE AND PRINTS AREA OF CIRCLE

def AreaofCirc(rad):
    pi = 3.14
    Area= pi * rad*rad
    print(Area)

def main():
    r = float(input("Enter the radius of circle: "))
    print("The area of the circle is: ")
    AreaofCirc(r)
if __name__ == "__main__":
    main()