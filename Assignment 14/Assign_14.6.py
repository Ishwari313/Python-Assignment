# WRITE A LAMBDA FUNCTION WHICH ACCEPTS ONE NUMBER AND RETURN TRUE IF NO IS ODD OTHERWISE FALSE

OddNo = lambda No: True if (No % 2 !=0) else False

def main():
    val =0
    ret = 0

    val = int(input("Enter the Number: "))
    ret= OddNo(val)
    print(OddNo(ret))

if __name__ =="__main__":
    main()