class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available}"


class Library:
    def __init__(self):
        self.books = []
        self.students = []

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

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False

    def display_students(self):
        for student in self.students:
            print(student)


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"Member ID: {self.student_id}, Name: {self.name}"


# Example usage:
book1 = Book(1, "Let us C", "Yashavant Kanetkar")
book2 = Book(2, "Programming with JAVA", "Bala gur")
book3 = Book(3, "Wings of Fire", "A.P.J.Abdul Kalam")

student1 = Student(501, "Sujana")
student2 = Student(502, "Suma")
student3 = Student(503, "Sai")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_student(student1)
library.add_student(student2)
library.add_student(student3)
print("Books in the library:")
library.display_books()

print("\nMembers in the library:")
library.display_students()







