def NameLength(name):
    count = 0
    for char in name:
        count += 1
    return count


def main():
    name = input("Enter your name: ")
    length = NameLength(name)
    print("Length of the name is:", length)


if __name__ == "__main__":
    main()
