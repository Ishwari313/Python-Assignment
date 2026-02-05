'''
Write a program which accepts a file name from the user and counts how many lines are present in the file
'''

def main():

    Filename = input("Enter the filename:")

    fobj = open(Filename,"r")

    count = 0

    for line in fobj:
        count+=1

    fobj.close()

    print("Total Lines in",Filename,"=",count)

if __name__ =="__main__":
    main()