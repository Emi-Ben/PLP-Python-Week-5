# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self.__price = price  # Private attribute for encapsulation

    # Getter for the private attribute
    def get_price(self):
        return self.__price

    # Setter for the private attribute
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be positive.")

    # Method to display smartphone details
    def display_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.__price}"

# Derived Class: AdvancedSmartphone
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, price, os, camera_megapixels):
        super().__init__(brand, model, price)  # Call to the base class constructor
        self.os = os
        self.camera_megapixels = camera_megapixels

    # Overriding the display_details method to include additional features
    def display_details(self):
        basic_details = super().display_details()
        return f"{basic_details}, OS: {self.os}, Camera: {self.camera_megapixels}MP"

    # Additional method
    def take_photo(self):
        return f"{self.model} takes stunning photos with its {self.camera_megapixels}MP camera!"

# Example usage
# Create an object of the base class
basic_phone = Smartphone("Nokia", "3310", 50)
print(basic_phone.display_details())
basic_phone.set_price(45)  # Update the price
print(f"Updated Price: ${basic_phone.get_price()}")

# Create an object of the derived class
smartphone = AdvancedSmartphone("Samsung", "Galaxy S23", 999, "Android", 230)
print(smartphone.display_details())
print(smartphone.take_photo())















# Base Class: Superhero
class Superhero:
    def __init__(self, name, alias, power_level):
        """
        Initialize a superhero with a name, alias, and power level.
        """
        self.name = name  # Public attribute
        self.alias = alias  # Public attribute
        self.__power_level = power_level  # Private attribute for encapsulation

    # Getter for private attribute
    def get_power_level(self):
        """
        Returns the superhero's power level.
        """
        return self.__power_level

    # Setter for private attribute
    def set_power_level(self, power_level):
        """
        Updates the superhero's power level if it's positive.
        """
        if power_level > 0:
            self.__power_level = power_level
        else:
            print("Power level must be positive!")

    # Method to display superhero details
    def display_details(self):
        """
        Returns a string representation of the superhero's details.
        """
        return f"Name: {self.name}, Alias: {self.alias}, Power Level: {self.__power_level}"

    # Method to demonstrate superhero action
    def save_the_day(self):
        """
        Simulates the superhero saving the day.
        """
        return f"{self.alias} is saving the day with their heroic deeds!"


# Derived Class: FlyingSuperhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, alias, power_level, flight_speed):
        """
        Initialize a flying superhero with additional flight speed attribute.
        """
        super().__init__(name, alias, power_level)  # Call to base class constructor
        self.flight_speed = flight_speed  # New attribute for flying speed

    # Overriding the save_the_day method to include flying ability
    def save_the_day(self):
        """
        Simulates the flying superhero saving the day.
        """
        return f"{self.alias} is soaring through the skies at {self.flight_speed} mph to save the day!"

    # Overriding the display_details method
    def display_details(self):
        """
        Returns a string representation of the flying superhero's details.
        """
        basic_details = super().display_details()  # Call to base class method
        return f"{basic_details}, Flight Speed: {self.flight_speed} mph"


# Main program to test the classes
if __name__ == "__main__":
    # Create a basic superhero
    hero1 = Superhero("Peter Parker", "Spider-Man", 85)
    print(hero1.display_details())
    print(hero1.save_the_day())

    # Update power level using setter
    hero1.set_power_level(90)
    print(f"Updated Power Level: {hero1.get_power_level()}")

    print("\n" + "="*50 + "\n")

    # Create a flying superhero
    hero2 = FlyingSuperhero("Clark Kent", "Superman", 100, 500)
    print(hero2.display_details())
    print(hero2.save_the_day())

















# Base Class: Book
class Book:
    def __init__(self, title, author, genre, pages):
        """
        Initialize a book with title, author, genre, and number of pages.
        """
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self.genre = genre  # Public attribute
        self.pages = pages  # Public attribute

    # Method to display book details
    def display_details(self):
        """
        Returns a string representation of the book's details.
        """
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Pages: {self.pages}"

    # Method to simulate reading the book
    def read_book(self):
        """
        Simulates reading the book.
        """
        return f"You start reading '{self.title}' by {self.author}. Happy reading!"

# Example usage
if __name__ == "__main__":
    # Create a book instance
    my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 218)

    # Display book details
    print(my_book.display_details())

    # Simulate reading the book
    print(my_book.read_book())
