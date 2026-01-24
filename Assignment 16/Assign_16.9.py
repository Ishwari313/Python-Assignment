''''
Write a program which display first 10 even numbers on screen.
'''

def DisplayEven():
    for i in range(1,11):
        if i %2==0:
            print(i)
    
def main():
    DisplayEven()
if __name__ =="__main__":
    main()
