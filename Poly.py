# Base Class: Book
class Book:
    def __init__(self, title, author, genre, pages):
        """
        Initialize a book with title, author, genre, and number of pages.
        """
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self.genre = genre  # Public attribute
        self.__pages = pages  # Private attribute for encapsulation

    # Getter for private attribute
    def get_pages(self):
        """
        Returns the number of pages in the book.
        """
        return self.__pages

    # Setter for private attribute
    def set_pages(self, pages):
        """
        Updates the number of pages if the value is positive.
        """
        if pages > 0:
            self.__pages = pages
        else:
            print("Pages must be a positive number!")

    # Method to display book details
    def display_details(self):
        """
        Returns a string representation of the book's details.
        """
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Pages: {self.get_pages()}"

    # Method to simulate reading the book
    def read_book(self):
        """
        Simulates reading the book.
        """
        return f"You start reading '{self.title}' by {self.author}. Enjoy your journey through its pages!"

# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, genre, pages, file_size):
        """
        Initialize an eBook with additional file size attribute.
        """
        super().__init__(title, author, genre, pages)  # Call to the base class constructor
        self.file_size = file_size  # Additional attribute for eBooks

    # Overriding the display_details method
    def display_details(self):
        """
        Returns a string representation of the eBook's details, including file size.
        """
        basic_details = super().display_details()  # Get details from the base class
        return f"{basic_details}, File Size: {self.file_size} MB"

    # Method to simulate downloading the eBook
    def download_book(self):
        """
        Simulates downloading the eBook.
        """
        return f"Downloading '{self.title}' by {self.author}... File size: {self.file_size} MB."

# Example Usage
if __name__ == "__main__":
    # Create a physical book
    physical_book = Book("1984", "George Orwell", "Dystopian", 328)
    print(physical_book.display_details())
    print(physical_book.read_book())

    # Create an eBook
    ebook = EBook("Sapiens", "Yuval Noah Harari", "History", 443, 15)
    print(ebook.display_details())
    print(ebook.read_book())
    print(ebook.download_book())
