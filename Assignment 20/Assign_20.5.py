'''
Design a Python application that creates two threads named Thread1 and Thread2

:-Thread1 should display numbers from  1 to 50
:-Thread2 should display numbers from 50 to 1 in reverse oredr
:-Ensure that:
    Thraed2 starts execution only after Thread1 has completed
:-Use appropraite Thread synchronization

'''
import threading

def Thread1():
    for i in range(1, 51):
        print("Thread1:", i)

def Thread2():
    for i in range(50, 0, -1):
        print("Thread2:", i)

def main():

    t1 = threading.Thread(target=Thread1, name="Thread1")
    t2 = threading.Thread(target=Thread2, name="Thread2")

    t1.start()
    t1.join()      #  Thread2 starts ONLY after Thread1 completes

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
