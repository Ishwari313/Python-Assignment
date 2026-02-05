'''
Write a program which accepts an existing file name through
command line aguments.create a new file named ABC.txt,and copies all
cntents from the given file into DEmo.txt.
'''
import sys

def main():
    if len(sys.argv) >3:
        print("Invalid Arguments..")
        return

    src = sys.argv[1]
    dest = sys.argv[2]

    
    f1 = open(src, "r")
    f2 = open(dest, "w")

   
    data = f1.read()
    f2.write(data)

   
    f1.close()
    f2.close()

    print("File copied successfully.")

main()
