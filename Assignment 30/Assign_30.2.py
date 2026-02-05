'''
Write a program which accepts a file name from the user
and counts the total number of words in that file
'''

def main():
    filename = input("Enter file name: ")

    fobj = open(filename, "r")
    data = fobj.read()
    fobj.close()

    words = data.split()
    print("Total number of words in", filename, ":", len(words))


if __name__ == "__main__":
    main()
