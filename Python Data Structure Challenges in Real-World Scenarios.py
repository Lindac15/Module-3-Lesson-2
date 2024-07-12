# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.
# Existing Library Data:
# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")] 
def add_book(library, book):
    if book not in library:
        library.append(book)
    else:
        print("Book already exists in the library")
    return library
print(add_book(library, ("The Catcher in the Rye", "J.D. Salinger")))
print(add_book(library, ("1984", "George Orwell")))
print(add_book(library, ("To Kill a Mockingbird", "Harper Lee")))
print(add_book(library, ("To Kill a Mockingbird", "Harper Lee")))
print(add_book(library, ("The Great Gatsby", "F. Scott Fitzgerald")))
print(add_book(library, ("The Great Gatsby", "F. Scott Fitzgerald")))
