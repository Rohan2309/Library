class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available books: ")
        for book in self.availableBooks:
            print(book)
        print()

    def lendBook(self, requestedBook):
        print()
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available.")
        print()

    def addBook(self, returnedBook):
        print()
        self.availableBooks.append(returnedBook)
        self.book = input()
        return self.book
        print()

class Customer:
    def requestBook(self):
        print()
        print("Enter the name of the book")
        self.book = input()
        return self.book
        print()

    def returnedBook(self):
        print()
        print("Enter the name of the book")
        self.book = input()
        return self.book
        print()

library = Library(['python book', 'java book', 'c++ book'])
customer = Customer()
while True:
    print("Enter 1 to display the available books ")
    print("Enter 2 to request for a books ")
    print("Enter 3 to return a books ")
    print("Enter 4 to exit ")
    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()