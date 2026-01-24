# WRITE A LAMBDA FUNCTION USING REDUCE() WHICH ACCEPTS A LIST OF NUMBERS AND RETURNS THE PRODUCT OF ALL ELEMENTS

from functools import reduce

Product = lambda No1, No2: No1 * No2

def main():
    Numbers = [2, 3, 4, 5, 6]

    RData = reduce(Product, Numbers)

    print("Product of all elements:", RData)

if __name__ == "__main__":
    main()