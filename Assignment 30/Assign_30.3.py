'''
Write a program which accepts a file name from the user
and displays the contents of the file line by line on screen
'''

def main():
    filename = input("Enter file name: ")

    fobj = open(filename, "r")

    for line in fobj:
        print(line, end="")   # end="" → avoids extra blank line

    fobj.close()


if __name__ == "__main__":
    main()
