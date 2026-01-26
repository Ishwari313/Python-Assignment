'''
Design a Python application that ceates two thread

:- Thread 1 should calculate and Display the maximum element from an list
:- Thread 2 should calculate and display the minimum element from the same list
:- The list should be accepted from the user
'''

import threading

def FindMax(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    print("\nMaximum Element:", max_val)

def FindMin(lst):
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    print("Minimum Element:", min_val)

def main():
    lst = []
    N = int(input("Enter how many numbers you want to enter: "))

    for i in range(N):
        lst.append(int(input(f"Enter number {i+1}: ")))

    t1 = threading.Thread(target=FindMax, args=(lst,))
    t2 = threading.Thread(target=FindMin, args=(lst,))

 
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
