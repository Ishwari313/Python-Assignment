# WRITE A PROGRAM WHICH ACCEPTS ONE NUMBER AND PRINTS BINARY EQUIVALENT
def DecimalToBinary(No):

    rev_bin = 0

    if No == 0:
        return 0

    while No > 0:
        rem = No % 2
        rev_bin = rev_bin * 10 + rem
        No = No // 2

    # reverse again to get correct binary
    binary = 0
    while rev_bin > 0:
        digit = rev_bin % 10
        binary = binary * 10 + digit
        rev_bin = rev_bin // 10

    return binary


def main():
    Num = int(input("Enter a number: "))
    print("Binary =", DecimalToBinary(Num))


if __name__ == "__main__":
    main()
