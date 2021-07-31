from datetime import datetime
from datetime import timedelta
from datetime import date

bookslist = ['python', 'ruby', 'swift', 'java', 'html']
booksAuthor = {
    bookslist[0] : 'Author 1',
    bookslist[1] : 'Author 2',
    bookslist[2] : 'Author 3',
    bookslist[3] : 'Author 4',
    bookslist[4] : 'Author 5',
}
booksPrice = {
    bookslist[0] : 15,
    bookslist[1] : 10,
    bookslist[2] : 15,
    bookslist[3] : 20,
    bookslist[4] : 20,
}


booksExactName = str("")
borrowedDate = date.today()
    
deadline = borrowedDate + timedelta(days=10)

returnDate = date.today()

fineDate = deadline + timedelta(days=1)

# Function that display all the available books

def displayBooks():
    print("List of available books for borrowing")
    for books in bookslist:
          print("Book Name : " + books)


#Function that takes borrower Name borrower Book name and display books price, borrowed date, returning date. 

def borrowBooks():
    borrowerName = input("Enter your Name : ")
    
    borrowedBook = input("Enter the name of the books which you want to borrow: ")


    global booksExactName
    booksExactName = borrowedBook.lower()

    bookslist.remove(booksExactName)
    price = booksPrice.get(booksExactName)

    print(f"""
    Dear {borrowerName}, You have sucessfully borrowed!

    Book Name : {borrowedBook} 

    Price : {price}

    Borrowed Date : {borrowedDate}

    Returning Date : {deadline}

    Dear customer, You are requested to return the book before returning date otherwise you are charge with fine. 
    Thank you, Enjoy your day by reading.
    """)


#Function that take returner Name and returning Book name and display returned date and check wether fine is charged or not 

def returnBooks():
    returnName = input("Enter your Name : ")
    returnBook = input("Enter your return Books name : ")

    nameModify = returnBook.lower()

    


    if booksExactName == returnBook:
        print(f"""
        Dear {returnName}, You have sucefully return your Books!

        Book Name : {returnBook}

        Borrowed Date : {borrowedDate}

        Returned Date : {returnDate}

        Return Date Sheduled (Deadline) : {deadline}

        Dear customer, Thanks a lot for returning book on time.
        Enjoy your day...
        """)

    else:
        print("You never borrowed this book from this library. Check again..")

    
    if returnDate >= fineDate:
        print("Sorry you need to pay the Fine.")
    
    bookslist.append(nameModify)


#   Function that helps to continue the program again and again

def forContinue():

    while(True):
        print("Welcome to the world library. Enter Your choice to continue")
        print("1. Display all books available for borrowing")
        print("2. Borrow Your favourite books")
        print("3. Return a books")
        print("4. Continue")
        print("5. Exit")

        userChoice = int(input())

        if userChoice == 1:
            displayBooks()
        elif userChoice == 2:
            borrowBooks()
        elif userChoice == 3:
            returnBooks()
        elif userChoice == 4:
            forContinue()
            
        elif userChoice == 5:
            break




        
        else:
            print("Not a valid choice")




while(True):
    print("Welcome to the world library. Enter Your choice to continue")
    print("1. Display all books available for borrowing")
    print("2. Borrow Your favourite books")
    print("3. Return a books")
    print("4. Continue")
    print("5. Exit")

    userChoice = int(input())

    if userChoice == 1:
        displayBooks()
    elif userChoice == 2:
        borrowBooks()
    elif userChoice == 3:
        returnBooks()
    elif userChoice == 4:
        forContinue
    elif userChoice == 5:
        break 
    
    else:
        print("Not a valid choice")


