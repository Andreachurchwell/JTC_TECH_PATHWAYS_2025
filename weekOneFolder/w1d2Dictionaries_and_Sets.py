# Week 1 Day 2 Python Dictionaries and Sets

# 🗂 Python Dictionaries
# Think of a dictionary like a real-life dictionary: it has a word (key) and a definition (value).

# 🔘 Python Sets
# A set is like a bag of unique items — no duplicates allowed!

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

band2 = dict(vocals = 'Plant', guitar = 'Page')

print(band)
print(band2)
print('type==',type(band))
print('length==',len(band))

# How to access items
print(band['vocals'])
print(band.get('guitar'))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify if a key exisits
# will return booleans
print('guitar' in band)
print('triangle' in band)

# change values
band['vocals'] = 'Coverdale'
band.update({'bass': 'JPJ'})
print(band)


# Remove items
print(band.pop('bass'))  #will return the value thats been removed
print(band)

band['drums'] = 'Bonham'

print(band)

print(band.popitem()) #removes the last key value pair and returns a tuple
print(band)

# Delete and clear
band['drums'] = 'Bonham'
del band['drums']
print(band)

band2.clear()
print(band2)

del band2


# Copy Dictionaries

# (how not to!!)
# band2 = band
# print('this is a bad copy!')
# print(band2)
# print(band)

# band2['drums'] = "Dave"
# print(band)

# (the good way!!)
band2 = band.copy()
band2['drums'] = "Dave"
print('THIS IS THE GOOD COPY EXAMPLE')
print('band==',band)
print('band2==',band2)

# or use the dict() constructor function
band3 = dict(band)
print("GOOD COPY")
print(band3)


# NESTED DICTIONARIES

member1 = {
    "name": 'Plant',
    'instrument': 'vocals'
}
member2 = {
    "name": 'Page',
    'instrument': 'guitar'
}

band = {
    'member1': member1,
    'member2': member2
}
print('band ==', band)
print(band['member1']['name'])

# SETS
nums = { 1,2,3,4}
nums2 = set((1,2,3,4))
print('nums=',nums)
print('num2=',nums2)
print('type=',type(nums))
print('length=',len(nums))

# NO DUP ALLOWED
nums = { 1,2,2,3}
print(nums)

# TRUE is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3,4,0}
print(nums)

# check if a value is in a set
print(2 in nums)
# BUT u cant refer to an element in the set with an index position or a key

# add a new element to a set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)
# you can use update with lists, tuples, and dictionaries as well

# merge two sests to create a new set
one = {1,2,3}
two = {5,6,7}
myNewSet = one.union(two)
print(myNewSet)

# keep only the dupes
one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)

# keeping everything except the dupes
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
print(one)


# in class code along
empty_dict = {}
print(empty_dict)

student = {
    'name': 'Alice',
    'age': 20,
    'major': 'Computer Science'
}
print(student)

contact = dict( name = 'Bob', phone = '8999787', email ='bob@example')
print(contact)
# print(student['name'])
# print(student['age'])
print(student.get('age'))
print(student.get('gpa', 'Not available'))

student['age'] = 21
print(student)

del student['major']
print(student)

age = student.pop('age')
print(f'removed age: {age}')
print(student)


# Breakout Room ex 1
# # Initialize an empty shopping cart
# shopping_cart = {}

# # TODO: Add items to the shopping cart
# # Example: Add "apple" with quantity 3
# # shopping_cart["apple"] = 3
# shopping_cart['apple'] = 3
# # TODO: Update quantities of existing items
# # Example: Increase quantity of "apple" to 5
# # shopping_cart["apple"] = 5
# shopping_cart['apple'] = 5
# # TODO: Remove an item from the cart
# # Example: Remove "apple"
# # del shopping_cart["apple"]
# del shopping_cart['apple']

# # TODO: Print out the contents of the cart
# print("Shopping cart contents:")
# print(shopping_cart)

# python methods 

inventory = {
    'apples' : 25,
    'bananas' : 12,
    'oranges' : 32,
    'pears' : 15
}

print(inventory)
keys = inventory.keys()
print(f'Keys: ', keys)

values = inventory.values()
print(f'Values: ', values)

items = inventory.items()
print(f'Items: {items}') 

print('apples' in inventory)
print('grapes' in inventory)

new_items = {
    'grapes': 20,
    'apples' : 30
}
inventory.update(new_items)
print(inventory)

student = {
    'name': 'alice',
    'age' : 20,
    'major' : 'compScience',
    'gpa' : 3.8
}

print('iterating thru keys:')
for key in student:
    print(key)

print('iterating thru value:')
for value in student.values():
    print(value)

print('iterating thru key val pairs')
for key, value in student.items():
    print(f'{key}: {value}')

squares = {x: x**2 for x in range(1,6)}
print(squares)


student = {
    'name': 'alice',
    'age' : 20,
    'major' : 'compScience',
    'gpa' : 3.8
}

string_values = {
    k: v.upper() for k, v in student.items() if isinstance(v,str)
}

print(string_values)

# Dictionary with student names as keys and scores as values
gradebook = {
    
    "Alice": 85,
    "Bob": 72,
    "Charlie": 58
    

}

# TODO: Calculate the average score
# Hint: use sum() and len()

average_score = sum(gradebook.values()) / len(gradebook)

# TODO: Find the highest score
# Hint: use max() on gradebook.values()

highest_score = max(gradebook.values())

# TODO: Create a dictionary with only passing students (score >= 60)
# look this code up later!!!!!!!!!!!! passing_students
passing_students = {
    name: score for name, score in gradebook.items() if score >= 60
} 

# Print results
print("Average score:", average_score)
print("Highest score:", highest_score)
print("Passing students:", passing_students)



# SETS IN CLASS
empty_set = set()
print(empty_set)
print(type({}))

fruits = {'apple', 'banana', 'orange', 'apple'}
print(fruits)

numbers = set([1,2,3,2,1])
print(numbers)

letters = set('hello')
print(letters)

setA = {1,2,3,4,5}
setB = {4,5,6,7,8}
unionSet = setA | setB
print(f'Union: {unionSet}')

intersecton_set = setA & setB
print(f'intersection', intersecton_set)

defferenceSet = setA - setB
print(f'difference a-b: {defferenceSet}')

symmetric_diff = setA ^ setB
print(f'summetric diff: {symmetric_diff}')

fruits = {'apple', 'banana', 'orange'}
print(fruits)
fruits.update(['mango', 'kiwi'])
print(fruits)
fruits.remove('apple')
print(fruits)
fruits.discard('watermelon')
fruits.pop()
print(fruits)
fruits.add('grape')
print(fruits)

# Sets of students enrolled in each course
course_a_students = {
     "Alice", "Bob", "Charlie"
}

course_b_students = {
     "Bob", "Diana", "Eve"
}

# TODO: Find students enrolled in both courses
both_courses = course_a_students & course_b_students

# TODO: Find students enrolled in either course
either_course = course_a_students | course_b_students

# TODO: Find students enrolled in course A but not course B
only_a = course_a_students - course_b_students

# TODO: Find students enrolled in course B but not course A
only_b = course_b_students - course_a_students

# Print results
print("Both courses:", both_courses)
print("Either course:", either_course)
print("Only in Course A:", only_a)
print("Only in Course B:", only_b)

# HASHTABLES

coordinates = {(0,0): 'origin', (1,0): 'unit x', (0,1): 'unit y'}
print(coordinates[(0,0)])

try:
    badDict = {[1,2]: 'value'}
except TypeError as e:
    print(f'Error: {e}')

mixDict = {42: 'answer', 'key': 'value', 3.14: 'pi'}
print(mixDict)

def countWords(text):
    words = text.lower().split()
    wordCount = {}
    for word in words:
        word = word.strip('.,!?;:"\'()[]{00}')
        print('this is word right now==', f'processing word {word}')
        if word in wordCount:
            wordCount[word] += 1
        else: 
            wordCount[word] = 1
        print('this is the current word count====', f'the current word count is {wordCount}')
    return wordCount

sample_text = 'Python is amazing. Python is also easy to learn. Python is a versatile lang.'
wordFreq = countWords(sample_text)
print(wordFreq)


responses = [
    'javascript','python', 'java', 'python', 'javascript', 'c++', 'go', 'rust', 'javascript'
]

uniquelan = set(responses)
print(f'unique lang: {uniquelan}')
langCount = {}
for lang in responses:
    langCount[lang] = langCount.get(lang, 0) + 1
print(langCount)


def group_by_domain(email_list):
    """
    Takes a list of email addresses and returns a dictionary
    where keys are domains and values are lists of usernames.
    """
    domain_dict = {}

    for email in email_list:
        username, domain = email.split('@')
        if domain not in domain_dict:
            domain_dict[domain] = []
        domain_dict[domain].append(username)

    # TODO: Fill in logic to populate domain_dict

    return domain_dict


# Example input (students can add their own)
emails = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "carol@gmail.com",
    "dave@outlook.com"
]

# Call the function and print the result
result = group_by_domain(emails)
print(result)


# def countLetters(text):
#     text = text.lower()  # Make everything lowercase
#     letterCount = {}

#     for index, letter in enumerate(text):
#         print(f"Step {index + 1}: Checking letter '{letter}'")

#         if letter.isalpha():  # Only count letters, not spaces or punctuation
#             if letter in letterCount:
#                 letterCount[letter] += 1
#             else:
#                 letterCount[letter] = 1

#             print(f"Updated count: {letter} = {letterCount[letter]}")
#         else:
#             print(f"Skipping '{letter}' (not a letter)")

#         print(f"Current state of letterCount: {letterCount}\n")

#     return letterCount

# sample_text = "Hello, World!"
# letterFreq = countLetters(sample_text)
# print("Final letter frequencies:", letterFreq)