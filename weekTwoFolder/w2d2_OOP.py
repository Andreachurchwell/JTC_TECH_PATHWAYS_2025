# # 🌟 OOP Basics in Python
# # Object-Oriented Programming (OOP) is a programming style based on objects—data structures that contain data (attributes) and functions (methods).
# # 🧱 1. Core Concepts of OOP
# # Class – A blueprint for creating objects.
# # Object – An instance of a class.
# # Attributes – Variables that belong to an object.
# # Methods – Functions that belong to an object.
# # __init__ Method – A special method that initializes an object (constructor).
# # self – Refers to the current instance of the class.


# #  Principles of OOP
# # Encapsulation – Keeping data and methods that work on that data in one place (a class).
# # Abstraction – Hiding the complex parts and showing only what’s necessary.
# # Inheritance – A class can inherit attributes and methods from another class.
# # Polymorphism – Different classes can use the same method name but behave differently.


# # Why Use OOP?
# # Organizes code better.
# # Reusable components.
# # Easier to manage complex programs.
# # Makes the code more readable and maintainable.


# # OOP approach using a Restaurant class
# class Restaurant:
#     """A class to represent a restaurant with its details."""
    
#     def __init__(self, name):
#         """Initialize a restaurant with a name and default values."""
#         self.name = name
#         self.addresses = []
#         self.menu_url = ''
#         self.hours = {
#             'Sunday': [0, 0],
#             'Monday': [0, 0],
#             'Tuesday': [0, 0],
#             'Wednesday': [0, 0],
#             'Thursday': [0, 0],
#             'Friday': [0, 0],
#             'Saturday': [0, 0],
#         }
    
#     def update_hours(self, day, opening, closing):
#         """Update the opening and closing hours for a specific day."""
#         hours_for_day = self.hours[day]
#         hours_for_day[0] = opening
#         hours_for_day[1] = closing
    
#     def is_open(self, day, time):
#         """Check if the restaurant is open at a specific time on a specific day."""
#         hours_for_day = self.hours[day]
#         return hours_for_day[0] < time < hours_for_day[1]

# # Creating a restaurant using our class
# islands = Restaurant('Islands')
# spudz = Restaurant('Spudz')

# # Using the methods
# islands.update_hours('Wednesday', 8, 17)
# print(islands.hours)
# print(f"Is {islands.name} open at noon on Wednesday? {islands.is_open('Wednesday', 12)}")
# print(f"Is {islands.name} open at 7pm on Wednesday? {islands.is_open('Wednesday', 19)}")

# # Notice how each restaurant has its own data
# spudz.update_hours('Monday', 10, 22)
# print(f"{islands.name} Monday hours: {islands.hours['Monday']}")
# print(f"{spudz.name} Monday hours: {spudz.hours['Monday']}")




# # OOP approach using a Restaurant class
# class Restaurant:
#     """A class to represent a restaurant with its details."""
    
#     def __init__(self, name):
#         """Initialize a restaurant with a name and default values."""
#         self.name = name
#         self.addresses = []
#         self.menu_url = ''
#         self.hours = {
#             'Sunday': [0, 0],
#             'Monday': [0, 0],
#             'Tuesday': [0, 0],
#             'Wednesday': [0, 0],
#             'Thursday': [0, 0],
#             'Friday': [0, 0],
#             'Saturday': [0, 0],
#         }
    
#     def update_hours(self, day, opening, closing):
#         """Update the opening and closing hours for a specific day."""
#         hours_for_day = self.hours[day]
#         hours_for_day[0] = opening
#         hours_for_day[1] = closing
    
#     def is_open(self, day, time):
#         """Check if the restaurant is open at a specific time on a specific day."""
#         hours_for_day = self.hours[day]
#         return hours_for_day[0] < time < hours_for_day[1]

# # Creating a restaurant using our class
# islands = Restaurant('Islands')
# spudz = Restaurant('Spudz')

# # Using the methods
# islands.update_hours('Wednesday', 8, 17)
# print(islands.hours)
# print(f"Is {islands.name} open at noon on Wednesday? {islands.is_open('Wednesday', 12)}")
# print(f"Is {islands.name} open at 7pm on Wednesday? {islands.is_open('Wednesday', 19)}")

# # Notice how each restaurant has its own data
# spudz.update_hours('Monday', 10, 22)
# print(f"{islands.name} Monday hours: {islands.hours['Monday']}")
# print(f"{spudz.name} Monday hours: {spudz.hours['Monday']}")



# class Student:
    
#     def __init__(self, name, student_id, gpa=0.0):
#         self.name = name
#         self.student_id = student_id
#         self.gpa = gpa
#         pass

#     def is_honor_roll(self):
#         if self.gpa >= 3.5:
#             return True
#         else:
#             return False
    
#     def update_gpa(self, new_gpa):
#         self.gpa = new_gpa


# student1 = Student('Juan', 123, 4.0)
# student2 = Student('Andrea', 345, 2.9)
# print(f'{student1.name} id: {student1.student_id} honorstudent: {student1.is_honor_roll()}')
# print(f'{student2.name} id: {student2.student_id}  honorstudent: {student2.is_honor_roll()}')
# student2.update_gpa(3.5)
# print(f'After update: {student2.name} honor roll: {student2.is_honor_roll()}')

class Bank_Account:
    bank_name = 'Python National Bank'
    accountTotal = 0
    

    def __init__(self, acct_num, owner_name, balance=0):
        self.acct_num = acct_num
        self.owner_name = owner_name
        self.balance = balance
        self.transactions = []

        self.transactions.append(f'Account opened with ${balance}.')
        Bank_Account.accountTotal += 1

    def deposit(self, amount):
        if amount <= 0:
            print('Error: Deposit must be a positive number amount.')

        self.balance += amount
        self.transactions.append(f'Deposited: ${amount}')
        return True
    
    def withdrawl(self, amount):
        if amount <= 0:
            print('Error: Withdrawl amount must be a positive number amount.')
            return False
        
        if amount > self.balance:
            print('Error: insufficent funds')
            return False
        
        self.balance -= amount
        self.transactions.append(f'Withdrawl: ${amount}')
        return True
    
    def get_balance(self):
        return self.balance
    
    def print_trans(self):
        print(f'Transaction history for account {self.acct_num}: ')

        for transaction in self.transactions:
            print(f'- {transaction}')
        print(f'Current Balance: ${self.balance}')

alice_acct = Bank_Account('123', 'Alice Adams', 1000)
bob_acct = Bank_Account('456', 'Bob Bell', 2000)

print(alice_acct.balance)
print(bob_acct.balance)
# Perform some transactions
alice_acct.deposit(500)
bob_acct.withdrawl(200)
alice_acct.withdrawl(1200)  # Should fail - insufficient funds
alice_acct.withdrawl(800)   # Should succeed

# Print information
print(f"{alice_acct.owner_name}'s balance: ${alice_acct.get_balance()}")
print(f"{bob_acct.owner_name}'s balance: ${bob_acct.get_balance()}")

# Print transaction history
alice_acct.print_trans()

# Demonstrate class attribute
print(f"Both accounts are with {Bank_Account.bank_name}")
print(f"Alice's bank: {alice_acct.bank_name}")
print(f"Bob's bank: {bob_acct.bank_name}")
print('total num of accts==',Bank_Account.accountTotal)

# this class Book was a breakout room activity
# class Book:
#     def __init__(self, title, author, pages, yearPub):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.yearPub = yearPub
#         self.checkedOut = False
#         self.rating = []


#     def checkout(self):
#         if not self.checkedOut:
#             self.checkedOut = True
#             print(f'{self.title} has been checked out!')
#         else:
#             print(f'{self.title} is already checked out!')

#     def returnBook(self):
#         if self.checkedOut:
#             self.checkedOut = False
#             print(f'{self.title} has been returned.')

#         else:
#             print(f'{self.title} hasnt been checked out.')
    
#     def addReview(self, rating):
#         if 0 <= rating <= 5:
#             self.rating.append(rating)
#             print(f'Here is the review rating {rating}')
#         else:
#             print('Rating should be scored 0-5')

    
#     def getRatingAverage(self):
#         if self.rating:
#             return sum(self.rating) / len(self.rating)
#         else:
#             return None
        
# library = [
#      Book('abc', 'def', 500, 1990) 
#      ]

# book = library[0]
# print(library[0].checkedOut)
# # book.checkedOut()
# print("Checked out?", book.checkedOut)  # Should be False
# # Check it out
# book.checkout()
# # Check again
# print("Checked out?", book.checkedOut)  # Should be True
# # Return the book
# book.returnBook()
# # Check again
# print("Checked out?", book.checkedOut) 

# this code below was the instructors class book, and its alot better!

# Completed Breakout Code

# class Book:
#     def __init__(self, title, author, pages, year):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#         self.checked_out = False
#         self.reviews = []  # List of dictionaries with name, rating, text
    
#     def check_out(self):
#         if self.checked_out:
#             print(f"Sorry, {self.title} is already checked out.")
#             return False
#         self.checked_out = True
#         print(f"{self.title} has been checked out.")
#         return True
    
#     def return_book(self):
#         if not self.checked_out:
#             print(f"{self.title} is not checked out.")
#             return False
#         self.checked_out = False
#         print(f"{self.title} has been returned.")
#         return True
    
#     def add_review(self, reviewer_name, rating, review_text=""):
#         if rating < 1 or rating > 5:
#             print("Rating must be between 1 and 5.")
#             return False
        
#         review = {
#             "reviewer": reviewer_name,
#             "rating": rating,
#             "text": review_text
#         }
#         self.reviews.append(review)
#         print(f"Review added for {self.title}.")
#         return True
    
#     def get_average_rating(self):
#         if not self.reviews:
#             return "No reviews yet."
        
#         total = sum(review["rating"] for review in self.reviews)
#         average = total / len(self.reviews)
#         return round(average, 1)
    
#     def book_info(self):
#         status = "Checked out" if self.checked_out else "Available"
#         avg_rating = self.get_average_rating()
#         rating_text = f"Average rating: {avg_rating}" if avg_rating != "No reviews yet." else "No reviews yet"
        
#         return f"{self.title} by {self.author} ({self.year}) - {status} - {rating_text}"

# # Create some books
# book1 = Book("The Hobbit", "J.R.R. Tolkien", 295, 1937)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 281, 1960)
# book3 = Book("1984", "George Orwell", 328, 1949)

# # Demonstrate functionality
# book1.check_out()
# book2.check_out()
# book2.check_out()  # Should say already checked out
# book2.return_book()

# book1.add_review("Alice", 5, "Amazing adventure!")
# book1.add_review("Bob", 4, "Really enjoyed it.")
# book2.add_review("Charlie", 5, "Classic for a reason")

# # Display book information
# print("\nLibrary Catalog:")
# for book in [book1, book2, book3]:
#     print(book.book_info())



        
        
        

      