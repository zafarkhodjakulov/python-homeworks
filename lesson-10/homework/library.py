class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} (Borrowed: {'Yes' if self.is_borrowed else 'No'})"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added book: {title} by {author}.")

    def add_member(self, name):
        new_member = Member(name)
        self.members.append(new_member)
        print(f"Added member: {name}.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.borrow_book(book)
        print(f"{member_name} borrowed '{book_title}'.")

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)
        print(f"{member_name} returned '{book_title}'.")

    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        raise ValueError(f"Member '{name}' not found.")

    def __str__(self):
        return f"Library has {len(self.books)} books and {len(self.members)} members."

def main():
    library = Library()

    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")

    library.add_member("Alice")
    library.add_member("Bob")

    try:
        library.borrow_book("Alice", "The Great Gatsby")
        library.borrow_book("Bob", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
    except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
        print(f"Error: {e}")

    try:
        library.return_book("Alice", "The Great Gatsby")
        library.return_book("Bob", "1984")
    except (BookNotFoundException, ValueError) as e:
        print(f"Error: {e}")

    try:
        library.borrow_book("Alice", "Nonexistent Book")
    except BookNotFoundException as e:
        print(f"Error: {e}")

    try:
        library.borrow_book("Alice", "1984")
    except BookAlreadyBorrowedException as e:
        print(f"Error: {e}")

    try:
        library.borrow_book("Alice", "The Great Gatsby")
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Alice", "Extra Book")
    except MemberLimitExceededException as e:
        print(f"Error: {e}")

    print(library)
    for member in library.members:
        print(member)
    for book in library.books:
        print(book)

