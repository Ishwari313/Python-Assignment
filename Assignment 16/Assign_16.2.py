'''
WRITE A PROGRAM WHICH CONTAINS ONE FUNCTIN NAMED AS ChkNum()
WHICH ACCEPTS ONE PARAMETER AS NUMBER.IF NUMBER IS EVEN THEN IT 
SHOULD DISPLAY "EVEN NUMBER" OTHERWISE DISPLAY "ODD NUMBER"
ON CONSOLE
'''

def ChkNum(No):
    if No % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"


def main():
    No = int(input("Enter the Number: "))
    ret = ChkNum(No)
    print(ret)


if __name__ == "__main__":
    main()