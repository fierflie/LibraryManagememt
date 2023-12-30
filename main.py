#import mysql.connector
from tkinter import Tk,Label,Entry,Button,messagebox

library = {
    "books": []
}

def add_book(Title, Author, ISBN):
    book = {"Title": Title, "Author": Author, "ISBN": ISBN, "available": True}
    library["books"].append(book)
    print(f"Book '{Title}' by {Author} added successfully.")

def display_books():
    books = library["books"]
    if not books:
        print("No books available in the library.")
    else:
        print("Available Books:")
        for book in books:
            if book["available"]:
                print(f"{book['Title']} by {book['Author']} (ISBN: {book['ISBN']})")

def borrow_book(title):
    for book in library["books"]:
        if book['Title'] == isbn and book["available"]:
            book["available"] = False
            print(f"You have successfully borrowed {book['Title']}.")
            return
    print("Book not available for borrowing.")

def return_book(ISBN):
    for book in library["books"]:
        if book["ISBN"] == ISBN and not book["available"]:
            book["available"] = True
            print(f"You have successfully returned {book['Title']}.")
            return
    print("Invalid ISBN or book is not borrowed.")
def search_book(input):
    matches=[]
    for book in library["books"]:
        if input.lower() in book["Title"].lower() or input.lower() in book["Author"].lower() or input.lower() in book["ISBN"].lower():
            matches.append(book)
    if not matches:
        print("No matching Books found")
    else:
        print("Matching Books:")
        for match in matches:
            print(f"{match['Title']} by {match['Author']}(ISBN:{match['ISBN']}")
#username=input()
#password=input()

# def authenticate_user(username,password):
#     attempts=3
#     while attempts>0:
#         username= input("Enter your username: ")
#         password= input("Enter your password: ")
#         if authenticate_user(username,password):
#             print("Authentication successful.\n Welcome to the Library ")
#             break
#         else:
#             attempts-=1
#             print(f"Authenticatiom failed.{attempts}{'attempts' if attempts>1 else 'attempt'}left")
#     if attempts==0:
#       print("Authentication failed. Exiting the program.")

def add_user(username,password):
    pass
def main_menu():
   #if authenticate_user(username,password):
    #    while True:
            print("Library Management System")
            print("1.Add Book")
            print("2.Search Book")
            print("3.Return Book")
            print("4.Borrow Book")
            print("5.Display available Books")
            print("6.Exit")
while True:
    main_menu()
    choice = input("Enter Your Choice: ")
    if choice == '1':
        add_book(input("enter Title: "),input("enter Author: "),input("ISBN: "))
    elif choice == '2':
        search_book(input("Search : "))
    elif choice == '3':
        return_book(input("enter the ISBN of the book: "))
    elif choice == '4':
        borrow_book(input("Enter the ISBN of the book:"))
    elif choice == '5':
        display_books()
    elif choice == '6':
        exit()
    else:
        print("Invalid Choice!!")


