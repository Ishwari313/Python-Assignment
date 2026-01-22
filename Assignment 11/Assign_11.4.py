def ReverseNumber(No):

    reverse = 0

    if No < 0:
        No = -No    # make positive for reversing

    while No != 0:
        digit = No% 10
        reverse = reverse * 10 + digit
        No = No // 10

    return reverse


def main():

    num = int(input("Enter a number: "))
    print("Reverse number:", ReverseNumber(num))


if __name__ == "__main__":
    main()
