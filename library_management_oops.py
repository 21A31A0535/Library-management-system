from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available Copies: {self.available_copies}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return True
        return False

    def display_books(self):
        for book in self.books:
            print(book)

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                return True
        return False

    def display_members(self):
        for member in self.members:
            print(member)

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member and book and book.available_copies > 0:
            member.borrowed_books.append(book)
            book.available_copies -= 1
            return True
        return False

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member and book and book in member.borrowed_books:
            member.borrowed_books.remove(book)
            book.available_copies += 1
            return True
        return False

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

class Member:
    def __init__(self, member_id, name, subscription_expiry=None):
        self.member_id = member_id
        self.name = name
        self.subscription_expiry = subscription_expiry
        self.borrowed_books = []

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Subscription Expiry: {self.subscription_expiry}"

    def renew_subscription(self, days=365):
        if self.subscription_expiry:
            self.subscription_expiry += timedelta(days=days)
        else:
            self.subscription_expiry = datetime.now() + timedelta(days=days)

# Example Usage:
book1 = Book(1, "Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin ", 5)
book2 = Book(2, "The Pragmatic Programmer: Your Journey to Mastery", "Dave Thomas", 3)
book3 = Book(3, "Effective Java", "oshua Bloch", 7)

member1 = Member(501, "Vicky")
member2 = Member(502, "Mickey")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_member(member1)
library.add_member(member2)

print("Books in the library:")
library.display_books()

print("\nMembers in the library:")
library.display_members()

# Borrowing and Returning Books
library.borrow_book(501, 1)
library.borrow_book(502, 2)
library.return_book(503, 1)

print("\nBooks after borrowing and returning:")
library.display_books()

# Member Subscription Renewal
member1.renew_subscription()
print("\nMember after subscription renewal:")
print(member1)

