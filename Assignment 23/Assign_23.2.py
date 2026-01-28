'''
Write a Python program to implement a class named BankAccount with 
the following requirements:
:>The class should contain two instance varibles:
    :>Name(Account holder Name)
    :>Amount(Account balance)
:>The class should contain one class variable:
    :>ROI(Rate of Interest),initialized to 10.5
:>Define a constructor (__init__)that accepts name and initial Amount
:>Implement the following instance methods:
    :>Display()-displays account holder name and current balance
    :>deposit()- accepts an amount from the user and adds it to balance
    :>Withdraw()- accepts an amount from the user and subtract it from 
                 balance 
                 (Ensure withdrawal is allowed only if sufficient balance exists)

    :>CalculteInterest()-calculate and retuns interest using formula:
        Interrest =(Amount *ROI)/100
:>Create multipla objects and demonstrate all methods
'''

class BankAccount:

    ROI=10.5

    def __init__(self,Name,Amonut):
        self.Name=Name
        self.Amount = Amonut

    def Display(self):
        print(f"Acount Holder: {self.Name}")
        print(f"Balance: {self.Amount}")
    
    def Deposit(self):
        amt=float(input("Enter amount:"))
        self.Amount +=amt
        print("Amount Deposited..")
        print("Updated Balamce:",self.Amount)

    def Withdraw(self):
        amt=float(input("Enter the amount to withdraw:"))
        if amt >self.Amount:
            print("Insufficient Balance:")
        else:
            self.Amount -=amt
            print("Withdraw Successfully....")
            print("Updated Balance:",self.Amount)
    
    def CalculateInterest(self):
        interest=(self.Amount *BankAccount.ROI )/100
        return interest
    
obj1 =BankAccount("Ishwari",1000)
obj2 =BankAccount("Rudra",2000)

print("\n--- Account 1 ---")
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
print("Interest Earned:", obj1.CalculateInterest())

print("\n--- Account 2 ---")
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
print("Interest Earned:", obj2.CalculateInterest())