'''
Design a Python application that creates three threads named small,Captital, and Digits

:- All threads should accepts a string as input
:- The Small thread should count and display the number of lowercase chrachters.
:- The Capital Thread should count and display the number of uppercase charactes
:- The Digits thread should count and display the number of numenric digits.
:- Each thread must also display:
    :-Thread ID
    :-Thread Name
'''
import threading

def SmallCount(s):
    small = sum(1 for ch in s if ch.islower())
    print("\nSmall Thread Output")
    print("Lowercase Count:", small)
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())

def CapitalCount(s):
    capital = sum(1 for ch in s if ch.isupper())
    print("\nCapital Thread Output")
    print("Uppercase Count:", capital)
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())

def DigitCount(s):
    digits = sum(1 for ch in s if ch.isdigit())
    print("\nDigit Thread Output")
    print("Digit Count:", digits)
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())

def main():
    s = input("Enter a string: ")

    t1 = threading.Thread(target=SmallCount, args=(s,), name="Small")
    t2 = threading.Thread(target=CapitalCount, args=(s,), name="Capital")
    t3 = threading.Thread(target=DigitCount, args=(s,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
