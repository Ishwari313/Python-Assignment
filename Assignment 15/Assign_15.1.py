# WRITE A LAMBDA FUNCTION USING MAP() WHICH ACCEPTS A LIST OF NUMBERSAND RETURN A LIST OF SQUARES OF EACH NUMBER

Square = lambda No1: No1*No1

def main():

    numbers=[1,2,3,4,5]

    MData = list(map(Square,numbers))
    print("The Square of no is:",MData)

if __name__=="__main__":
    main()