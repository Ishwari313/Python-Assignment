'''Write a program  which contains filter(), map(),reduce() in it.
Python application which contains one list of numbers .list contains
the numbers which are accepted from user.filter should filter out all
prime numbers. map functon will multiply each number by 2
reduce will return maximum no from that numbers
'''

from functools import reduce

def ChkPrime(No):
    if No < 2:
        return False
    for i in range(2, No // 2 + 1):
        if No % i == 0:
            return False
    return True


def main():
    lst = []
    N = int(input("How many numbers you want to enter: "))

    for i in range(N):
        num = int(input(f"Enter number {i+1}: "))
        lst.append(num)

    print("Input List =", lst)

    
    Fdata = list(filter(ChkPrime, lst))
    print("List after filter (prime numbers) =", Fdata)

 
    Mdata = list(map(lambda x: x * 2, Fdata))
    print("List after map (multiply by 2) =", Mdata)

   
    Rdata = reduce(lambda a, b: a if a > b else b, Mdata)
    print("Maximum number (reduce output) =", Rdata)


if __name__ == "__main__":
    main()
