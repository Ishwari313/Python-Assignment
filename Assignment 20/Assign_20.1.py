'''
Design a Python application that creates two separate threads named Even and Odd
:-The Even thread should display the first 10 even numbers
:-The Odd thred should display the first 10 odd numbers
:-Both threas  should execute independently using the threding module
:- Ensure proper thred creation and execution
'''

import threading
import time

def print_even():
    print("Even No:")
    for i in range(2,11,2):
        print(i)

def print_odd():
    print("Odd No:")
    for i in range(1,20,2):
        print(i)

def main():
    start_time=time.time()

    t1 = threading.Thread(target=print_even)
    t2 = threading.Thread(target=print_odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time =time.time()

    print("Time Required:",end_time-start_time)

if __name__ =="__main__":
    main()