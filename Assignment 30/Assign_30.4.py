'''
Write a program which accepts two file names from the user

    ->First file is existinf file
    ->Second is a new file

copy all contents from the first file into the second file

'''

import sys

def main():
    if len(sys.argv) > 3:
        print("Invalid arguments")
        return

    new_file = sys.argv[1]
    old_file = sys.argv[2]

    # Open old file in read mode
    fobj1 = open(old_file, "r")

    # Open new file in write mode
    fobj2 = open(new_file, "w")

    # Copy content
    data = fobj1.read()
    fobj2.write(data)

    fobj1.close()
    fobj2.close()

    print(" copied successfully.")

if __name__ == "__main__":
    main()
