# 1. Library Management System 
# • Description: Create a console application to manage a library's books. Implement classes for Book, Member, and Library. Include features to add, remove, and search for books, as well as borrowing and returning books by members.

# • OOP Concepts: Encapsulation (managing book and member data), Inheritance (different member types), and Polymorphism (handling different book formats).

class Book:
    def __init__(self,title,author,number_of_pages):
        self.title=title
        self.author=author
        self.no_of_pages=number_of_pages
        self.is_borrowed=False
    def __str__(self):
        return f"{self.title}\t\t:\t{self.author}"
    
class Member:
    member_id=1
    def __init__(self,name):
        self.name=name
        self.member_id=Member.member_id
        self.borrowed_book=[]
        Member.increase_member()
    @classmethod
    def increase_member(cls):
        cls.member_id+=1
    
    def borrow_book(self,book):
        if not book.is_borrowed:
            self.borrowed_book.append(book)
            book.is_borrowed=True
            print(f"{self.name} borrowed {book.title} book.")
        else:
            print(f"{book.title} has already been borrowed.")
    
    def return_book(self,book):
        if book in self.borrowed_book:
            self.borrowed_book.remove(book)
            book.is_borrowed=False
            print(f"{self.name} returned book {book.title}.")
        else:
            print(f"{self.name} have not borrowed book {book.title}.")
    

class Student(Member):
    def __init__(self, name):
        super().__init__(name)
        self.member_type="Student"
    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_book]
        return f'{self.name} \t {self.member_id} \t {borrowed_titles} \t{self.member_type}'

class Teacher(Member):
    def __init__(self, name):
        super().__init__(name)
        self.member_type="Teacher"
    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_book]
        return f'{self.name} \t {self.member_id} \t {borrowed_titles} \t{self.member_type}'
    
class Library:
    def __init__(self):
        self.books=[]
        self.members=[]

    def add_book(self,book):
        self.books.append(book)
    
    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("No such book.")
    def search(self,title):
        book_=[book for book in self.books if book.title.lower()==title.lower()]
        if book_:
            for book in book_:
                print(book)
        else:
            print(f"No book found with title {title}.")
    def add_member(self, member):
        self.members.append(member)

    def show_book(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("The list of books are:")
            for book in self.books:
                print(book)
        print()
    def show_member(self):
        if not self.members:
            print("No members of library.")
        else:
            print("The list of members are:")
            for member in self.members:
                print(member)
        print()

l=Library()
b1=Book("Harry Potter","J.K.Rowling",435)
b2=Book("Alice in borderland","Lewis Carrol",323)
b3=Book("David Copperfield","Charles Darwin",879)
l.add_book(b1)
l.add_book(b2)
l.add_book(b3)

s1=Student("Pragyan")
s2=Student("Rita")
t1=Teacher("Tek Ram")
t2=Teacher("Jack")
l.add_member(s1)
l.add_member(s2)
l.add_member(t1)
l.add_member(t2)

l.show_book()
l.show_member()

s1.borrow_book(b2)
t1.borrow_book(b3)

l.show_book()
l.show_member()
s1.return_book(b2)

l.search("Alice in BorderLand")