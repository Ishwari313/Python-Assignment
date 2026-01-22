#WRITE A PROGRAM WHICH ACCEPTS ONE NUMBER AND CHECKS WHETHER IT IS PALINDROME OR NOT

def Palindrom(No):
    org = No
    reverse = 0

    if No < 0:
        No = -No    # make positive for reversing

    while No != 0:
        digit = No% 10
        reverse = reverse * 10 + digit
        No = No // 10

    return reverse ==org


def main():

    num = int(input("Enter a number: "))

    if Palindrom(num):
        print("Palindrome")

    else:
        print("Not palindrome")


if __name__ == "__main__":
    main()
