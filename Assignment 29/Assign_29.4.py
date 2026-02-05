'''
Write a program which accepts two file name through 
Command line arguments and compares the contents of both files.
    -If both files contains the same contents display succes
    -Otherwise display Failure
'''
import sys

def main():
    if len(sys.argv) >3:
        print("Invalid Arguments")

file1 = sys.argv[1]
file2 = sys.argv[2]

f1obj= open(file1,"r")
f2obj = open(file2,"r")

data1=f1obj.read()
data2= f2obj.read()

f1obj.close()
f2obj.close()

if data1==data2:
    print("Success")
else:
    print("Failure")

if __name__ == "__main__":
    main()