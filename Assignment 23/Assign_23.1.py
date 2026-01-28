'''
Write a python program to implement a class named BookStore with the following Specifications:
:> The class should contain two instance variables:
    :>Name(Book Name)
    :>Author(Book Author)
:> The class should contain one class variable:
    :>NoOfBooks(initialize it to 0)

:>Define a constructor (__init__)thar accepts Name and Author
    and initializes instance variables.
:>Inside the constructor ,increment the class variable NoOfBooks by 1 whenever a new object is created
:>Implemet an instance method:
    :>Display()-should display book details in yhe format:
    :> <BookName> bu <Author> No of books: <NoOfBooks>
'''

class BookStore:
    NoOfBooks=0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author= Author
        BookStore.NoOfBooks +=1

    def display(self):
        print(f"{self.Name} by {self.Author} No of books:{BookStore.NoOfBooks}")
    
obj1=BookStore("Linux System Programmming","Robert Love")
obj1.display()

obj2=BookStore("C Programming","Dennis Ritchie")
obj2.display()