'''
Write a program which accepts a file name and one string from the user
and returns the frequency (count of occurences ) of that string in the filr
'''
def main():
    filename = input("Enter file name: ")
    Str= input("Enter string to search: ")

    fobj = open(filename, "r")
    data = fobj.read()
    fobj.close()

    # Count occurrences
    count = data.count(str)

    print("Frequency of '{}' is : {}".format(str, count))


if __name__ == "__main__":
    main()
