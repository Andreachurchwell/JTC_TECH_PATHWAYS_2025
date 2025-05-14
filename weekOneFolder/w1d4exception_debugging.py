# List of Errors:
# 1. AttributeError
# What it means: You're trying to access an attribute or method that doesn’t exist for that object.

# my_list = [1, 2, 3]
# my_list.upper()  # ❌ Lists don’t have an `upper()` method
# Fix: Check the type of the object and make sure you're using a valid method for it.

# 2. ImportError / ModuleNotFoundError
# What it means: Python can't find the module or object you're trying to import.
# import non_existing_module  # ❌
# Fix: Double-check the module name, spelling, or install the package using pip.

# 3. IndexError
# What it means: You're trying to access a list index that doesn't exist.
# my_list = [10, 20]
# print(my_list[5])  # ❌
# Fix: Check the length of the list using len() and make sure your index is valid.

# 4. KeyError
# What it means: You’re trying to access a dictionary key that doesn’t exist.
# my_dict = {"name": "Andrea"}
# print(my_dict["age"])  # ❌
# Fix: Use .get() or check if the key exists with in.

# 5. NameError
# What it means: You're trying to use a variable or function that hasn’t been defined.
# print(age)  # ❌ if `age` hasn't been defined
# Fix: Make sure all variables are spelled correctly and defined before you use them.


# 6. NotImplementedError
# What it means: This is a placeholder for code that hasn’t been written yet.
# def my_function():
#     raise NotImplementedError("Add your code here")
# Fix: Implement the missing code instead of raising this error.

# 7. StopIteration
# What it means: Raised when a loop or iterator has no more items.
# it = iter([1, 2])
# next(it)
# next(it)
# next(it)  # ❌ No more items
# Fix: Handle with a for loop or a try block.

# 8. SyntaxError
# What it means: The code doesn’t follow Python’s rules.
# if True
#     print("Hello")  # ❌ Missing colon
# Fix: Check for missing colons, parentheses, or other grammar rules.

# 9. IndentationError
# What it means: Your code is not properly indented.
# def say_hi():
# print("Hi")  # ❌ Should be indented
# Fix: Make sure blocks are indented consistently (usually 4 spaces).

# 10. ValueError
# What it means: A function got the right type of argument but with an invalid value.
# int("hello")  # ❌ Can’t convert to integer
# Fix: Check your input data and make sure values are valid.

# 11. TypeError
# What it means: You're using the wrong type of value for an operation.
# "2" + 2  # ❌ Can't add string and integer
# Fix: Use type conversion like int() or str() when mixing types.

# 12. RuntimeError
# What it means: Something went wrong while the program was running, but it doesn’t fit into a more specific category.
# def recurse():
#     return recurse()
# recurse()  # ❌ May raise a RuntimeError: maximum recursion depth exceeded
# Fix: This usually points to problems like infinite loops, recursion errors, or misuse of APIs. Read the error message carefully to narrow it down.

# 13. LogicError (Not a built-in error, but still important!)
# What it means: Your code runs without crashing, but it gives the wrong result due to a mistake in your logic.
# def is_even(n):
#     return n % 2 == 1  # ❌ This actually checks if it's odd
# Fix: Use print statements or debugging tools to trace your variables and logic step-by-step. Writing tests helps catch logic errors early!


# try / except Block in Python
# What it does:
# A try/except block lets you test code for errors and handle them gracefully instead of letting your whole program crash.

# Basic Structure:

# try:
#     # Code that might raise an error
# except SomeError:
#     # Code that runs *only if* there's an error
#  Example:

# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ValueError:
#     print("Oops! That's not a valid number.")
# except ZeroDivisionError:
#     print("Oops! You can't divide by zero.")
#  What happens:
# If the user types letters instead of a number → ValueError is caught.

# If the user types 0 → ZeroDivisionError is caught.

# If no error happens → it just runs normally.

#You can also catch any error:

# try:
#     # risky code
# except Exception as e:
#     print("Something went wrong:", e)
# Exception as e gives you the actual error message.

# # Bonus: else and finally

# try:
#     print("Trying code")
# except:
#     print("Something went wrong")
# else:
#     print("No errors occurred!")
# finally:
#     print("This will always run")
# else: runs only if no error occurs.

# finally: runs no matter what (good for cleaning up things).


# DAVE GRAY WALKTHRU TUTORIAL BELOW

# class JustNotCoolError(Exception):
#     pass

# x = 2
# try:
#     # print(x / 0) #change the 1 to 0 to see where the except raises error
#     # if not type(x) is str:
#     #     raise TypeError('only strings are allowed')
#     raise JustNotCoolError("this aint cool man")
# except NameError: 
#     print('nameError means something is prob undef')
# except ZeroDivisionError:
#     print('Please dont divide by zero.')
# except Exception as error:
#     print(error)
# else:
#     print('No Errors!!')
# finally:
#     print('I will print with or without an error!')

# BRO CODE WALKTHRu

# exception is an event that interrupts the flow of a program
# (ZeroDivError, TypeErr, Valerr)
# 1.try, 2.except, 3. finally

# try:
#     number = int(input('Enter a number: '))
#     print(1 / number)
# except ZeroDivisionError:
#     print('You cant divide by zero!')
# except ValueError:
#     print('Enter only numbers please!')
# except Exception:
#     print('Something went wrong!')
# finally:
#     print('Do some cleanup here')

    


# inventory = ['apple', 'banana', 'orange', 'grape']
# def ckorder(order):
#     for item in order:
#         print('item in order', item)
#         if item not in inventory:
#             return False
#     else:
#         return True
# order_1 = ['apple', 'kiwi']
# print(ckorder(order_1))

# inventory = {
#     1: 'apple',
#     2: 'nanana',
#     3: 'orange',
#     4: 'grape'
# }

# try:
#     userInput = input('Enter a item number (1-4)')
#     ordernum = int(userInput)
#     print(inventory[ordernum])
# except ValueError as e:
#     print('number please!')
# except KeyError as e:
#     print('THats not in the inventory')
# except Exception as e:
#     print('something went wrong')
#     print(type(e))
# else:
#     print('this only excutes when theres no errors')
# finally:
#     print('this runs no matter what')

# print(inventory[ordernum])

# def divide_inputs(input1, input2):

#     try:
#         num1 = float(input1)
#         num2 = float(input2)
#         return num1 / num2
#     except ValueError as valErr:
#         print('inputs should be a number!')
#     except ZeroDivisionError as e:
#         print('Cant divide by zero!!')


# def get_inputs():
#     input1 = input("Enter the first number: ")
#     input2 = input("Enter the second number: ")
#     result = divide_inputs(input1, input2)
#     print(result)

# get_inputs()


def validate_password(password):
    try:
        if len(password) < 8:
            return "Password must be at least 8 characters long."
        if not any(char.isupper() for char in password):
            return "Password must contain at least one uppercase letter."
        if not any(char.islower() for char in password):
            return "Password must contain at least one lowercase letter."
        if not any(char.isdigit() for char in password):
            return "Password must contain at least one number."
        
        return "Password is valid."

    except Exception as e:
        return f"An error occurred during validation: {e}"


user_password = input("Enter your password: ")
result = validate_password(user_password)
print(result)



