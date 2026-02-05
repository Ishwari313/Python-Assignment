'''
Wite a program which accepts a file name from the user and checks whether that file existes in current directory or not

'''
import os
def main():
    FileName = input("Enter the FileName:")

    Ret = os.path.exists(FileName)

    if (Ret == True):
        print("File is Exists")
    else:
        print("No such a file")

if __name__ =="__main__":
    main()