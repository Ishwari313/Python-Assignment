# WRITE A LAMBDA FUNCTION USING FILTER() WHICH ACCEPTS A LIST OF NUMBERS
# AND RETURNS THE COUNT OF EVEN NUMBERS

Even = lambda X: (X % 2 == 0)

def main():
    Numbers = [12, 15, 20, 33, 40, 55, 60, 71, 82]

    FData = list(filter(Even, Numbers))

    print("Count of even numbers:", len(FData))

if __name__ == "__main__":
    main()
