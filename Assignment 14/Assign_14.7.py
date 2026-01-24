# WRITE A LAMBDA FUNCTION WHICH ACCEPTS ONE NUMBER AND RETURN TRUE IF DIVISIBLE BY 5

Div = lambda No : True if (No % 5 ==0) else False

def main():
    val = 0
    ret = 0
    val= int(input("Enter the Number: "))
    ret=Div(val)
    print(Div(ret))

if __name__=="__main__":
    main()