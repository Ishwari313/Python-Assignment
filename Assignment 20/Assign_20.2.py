'''
Design a Python application that creats two thread

:- Thread 1 should calculate and display the maximum element from an list
:- Thread 2 should calculate and displsy the minimum element from the same list
:- The list should be accepted from the user
'''
import threading
import time

def Max(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    print("Maximum No:", maximum)

def Min(lst):
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    print("Minimum No:", minimum)
    
def main():
    
    lst=[]
    N=int(input("Enter how much No you want to enter: "))

    for i in range(N):
        Num=int(input(f"Enter The Number{i+1}:"))
        lst.append(Num)
    print("List is:",lst)

    start_time=time.time()

    t1=threading.Thread(target=Max,args=(lst,))
    t2= threading.Thread(target=Min,args=(lst,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time=time.time()

    print("Total Execution Time:",end_time-start_time)

if __name__=="__main__":
    main()