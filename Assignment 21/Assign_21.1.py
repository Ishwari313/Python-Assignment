'''
Design a Python application that creates two threads named Prime and NonPrime.
:-Both threads should accept a ist of integers
:-The Prime thread should display all prime Numbers from the list
:-The NonPrime thread should display all non prime numbers from the list
'''

import threading

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

def PrimeThread(lst):
    print("\nPrime Numbers:")
    for n in lst:
        if isPrime(n):
            print(n)

def NonPrimeThread(lst):
    print("\nNon-Prime Numbers:")
    for n in lst:
        if not isPrime(n):
            print(n)

def main():
    lst = []
    N = int(input("How many numbers you want to enter: "))

    for i in range(N):
        lst.append(int(input(f"Enter number {i+1}: ")))

    t1 = threading.Thread(target=PrimeThread, args=(lst,), name="Prime")
    t2 = threading.Thread(target=NonPrimeThread, args=(lst,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
