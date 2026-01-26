'''
Design a python application that creates two threads named EvenList and OddList
:-Both threads should accept a list of integers as input
:-The EvenList thread should:
    :-Extract all even elements from the list
    :-Calculate and display their sum

:- The OddList thread should:
    :-Extract all Odd elements from the list
    :-Calculate and display their sum

:- Threads should run concurrently
'''
import threading

def EvenList(lst):
    even_sum = 0
    print("\nEven Numbers:")
    for num in lst:
        if num % 2 == 0:
            print(num)
            even_sum += num
    print("Sum of Even Numbers:", even_sum)

def OddList(lst):
    odd_sum = 0
    print("\nOdd Numbers:")
    for num in lst:
        if num % 2 != 0:
            print(num)
            odd_sum += num
    print("Sum of Odd Numbers:", odd_sum)

def main():
    lst = []
    N = int(input("Enter how many numbers you want to store: "))

    for i in range(N):
        num = int(input(f"Enter the Number{i+1}:"))
        lst.append(num)
    print("list :", lst)

    t1 = threading.Thread(target=EvenList, args=(lst,))
    t2 = threading.Thread(target=OddList, args=(lst,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
