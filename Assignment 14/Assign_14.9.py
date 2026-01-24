# WRITE A LAMBDA FUNCTION EHICH ACCEPTS TWO NUMBERS AND RETURN MULTIPLICATION

Multi = lambda No1,No2 :No1*No2

def main():

    val1=0
    val2=0
    ret=0

    val1=int(input("Enter the first Number: "))
    val2 =int(input("Enter the Second Number:"))

    ret =(Multi(val1,val2))
    print("The Multiplication is:",ret)

if __name__ =="__main__":
    main()