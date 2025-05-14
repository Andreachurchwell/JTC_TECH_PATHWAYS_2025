# 🧠 Function Basics – Python Notes
# 📌 What is a function?
# A function is a block of reusable code that performs a specific task.

# ✅ Why use functions?
# To organize code

# To avoid repetition (DRY = Don't Repeat Yourself)

# To make code easier to read and test

# 🛠️ How to Define a Function

def function_name():
    # code block
    print("This is a function")


# 🧪 How to Call (Run) a Function

function_name()
# 📥 Functions with Parameters (Inputs)

def greet(name):
    print(f"Hello, {name}!")
    
greet("Andrea")
# 🎁 Functions that Return a Value

def add(a, b):
    return a + b

result = add(5, 3)
print("The result is:", result)


# 💡 Default Parameters

def greet(name="Friend"):
    print(f"Hello, {name}!")
    
greet()         # Output: Hello, Friend!
greet("Andrea") # Output: Hello, Andrea!


# 🔄 Combining It All – Function with Input, Logic, and Return

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # True
print(is_even(7))  # False


# 🧹 Pro Tip: Keep Functions Small and Focused
# Each function should do one thing well. If it's getting too long or confusing, break it into smaller functions.




# def greet():
#     print('HEllo WOrld!')
# greet()

# def countdown():
#     print('3')
#     print('2')
#     print('1')
#     print('GOOOO')
# countdown()
# print('runitagiain')
# countdown()


#breakout printpatter, in function, prints a tree

# def print_pattern():
#     print('*')
#     print('**')
#     print('***')
#     print('**')
#     print('*')

# print_pattern()

# def greetPerson(name):
#     print(f'Hello, {name}!')
# greetPerson('Andrea')




# def calcAreaRect(length, width):
#     area = length * width
#     print(f'area of a rectangle with length of {length} and width {width} is {area}.')
#     if length == width:
#         print('this is a square')

# calcAreaRect(6,4)
# calcAreaRect(5,5)
# calcAreaRect(6,76)


# def greetWmessage(name, message='how are you today?'):
#     print(f'hey, {name} {message}')

# greetWmessage('andrea')
    # """
    # Create a function that returns whether a person is a child, teenager, adult, or senior based on their age
    # Under 13: "[name] is a child."
    # 13-19: "[name] is a teenager."
    # 20-64: "[name] is an adult."
    # 65+: "[name] is a senior."
    # """

# def classify_person(name, age):
#     # Your code here
#     if age < 13:
#         print(f'{name} is {age}, a child.')
#     elif 13 <= age <= 19:
#         print(f'{name} is {age}, a teenager.')
#     elif 20 <= age <= 64:
#         print(f'{name} is {age}, an adult.')
#     else:
#         print(f'{name} is {age}, a senior.')


#     pass

# # Test cases
# classify_person("Alex", 10)
# classify_person("Jamie", 15)
# classify_person("Taylor", 30)
# classify_person("Morgan", 70)

# return values

# def addNums(a, b):
#     return a + b

# sumResult = addNums(5,3)
# print(f'the sum is: {sumResult}')


# print(f'10 + 20 = {addNums(10,20)}')  

# def get_user_info():
#     name  = 'andy'
#     age = 30
#     country = 'USA'
#     return name, age, country
# user = get_user_info()
# print(user)
# country = get_user_info()
# print(f' Lives in {country[2]}')


# def divideSafely(a, b):
#     if b != 0:
#         return a/b
#     else: 
#         return ('cant divide by 0')
        
     
    
# result1 = divideSafely(10,2)
# print(f' Result1 : {result1}')

# result2 = divideSafely(5,0)
# print(f' Result2 : {result2}')

# how a function can have conditonal logic
# teacher trying to seperate scores

# def gradeScore(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"
# print(f'ALice 85: {gradeScore(85)}')


# def sumList(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# myNums = [1,2,3,4,5]
# print(f'sum of {myNums} is {sumList(myNums)}')

# def calcAverage(numbers):
#     if not numbers:
#         return 0
#     total = sumList(numbers)

#     return total/len(numbers)

# testScores = [99,92,75,83]
# print(f"average score: {calcAverage(testScores)}")

# fruits = ['apple', 'banana', 'cherry']

# for fruit in fruits:
#     print(fruit)

# def print_items(items):
#     for item in items:
#         print(item)

# print_items(['dog', 'cat', 'bird'])

# def get_items(items):
#     result = []
#     for item in items:
#         if len(item) > 3:
#             result.append(item.upper())
#     return result

# print(get_items(['bird','dog', 'cat']))

# def excitedItems(words):
#     result = []
#     for word in words:
#          result.append(word + '!')
#     return result

# function named longestword, should take in a list of words as a parameter, 
# function should return the longests word,
#  if mult words are of the same length, return the first one


# def longest_word(words):
#     longest = ""  # Start with an empty string or None to track the longest word.
    
#     for word in words:
#         if len(word) > len(longest):  # Compare the length of current word with the longest
#             longest = word  # Update the longest word
    
#     return longest


