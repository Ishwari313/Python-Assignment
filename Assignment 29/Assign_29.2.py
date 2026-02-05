'''
Write a program which accepts a file name from the user,
opens that file, and display the entire contents on the console
'''
import os
def main():
    
    FileName= input("Enter the file name:")

    try:
        fobj = open(FileName,"r")
        data = fobj.read()
        print(data)
        fobj.close

    except:
        print("Not a such a file")

if __name__ =="__main__":
    main()