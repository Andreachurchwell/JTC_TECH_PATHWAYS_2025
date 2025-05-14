# test: turn louie to L*O*U*I*E*
# Empty string: Yes, you’ll need that to collect the final result.

# Loop through the string: Absolutely — you want to process each letter.

# Add * after each iteration: Right on! But don’t forget, you’ll only need to add the * between letters, not after the last one

def looper(word):
    new_word = ''
    for index in range(len(word)):
        letter = word[index].upper()  # Make the letter uppercase
        if index != len(word) - 1:  # Check if it's not the last letter
            new_word += letter + '*'  # Add * between letters
        else:
            new_word += letter  # Don't add * after the last letter
    return new_word

print(looper('louie'))

# def looping(word):
#     newloop = ''
#     for index in range(len(word)):
#         letter = word[index].upper()
#         newloop += letter
        
#         newloop +=  '$'
        
#     return newloop
# print(looping('andrea'))

# full_name = 'Andrea Elizabeth Churchwell'
# print(full_name[7:16])
# print(full_name)

# full_name = 'Andrea Elizabeth Churchwell'
# print(full_name[0] + ' ' + full_name[17])

# list = ['cooking', 'cats', 'nba', 'flowers', 'shopping']
# list.append('coding')
# print(list)
# list.remove('cooking')
# print(list)
# list.insert(0, 'eating')
# print(list)

# myDict = {
#     'name': 'Louie',
#     'age': 3,
#     'job': 'boss',
#     'city': 'Selmer'
# }
# myDict['sex'] = 'male'
# print(myDict)
# myDict['job'] = 'king'
# print(myDict)
# del myDict['age']
# print(myDict)

# favFoods = ['lobster', 'crab', 'pizza', 'pasta']
# for food in favFoods:
#     print(food)

# age = 25

# if age < 18:
#     print('youre a minor')
# else:
#     print('youre an adult')

# print(age)

# def addNum(num1,num2):
#     return num1 + num2

# result = addNum(1,4)
# print(result)


# 1. List Manipulation
# Task:
# Create a list of 5 random cities you want to visit.
# Remove one city from the list.
# Insert a new city at the beginning of the list.
# Sort the list in alphabetical order.
# Print the final list.

# cities = ['Dallas', 'LA', 'Montana', 'Miami']
# del cities[0]
# print(cities)
# cities.insert(0, "Jackson Hole")
# print(cities)
# cities.sort()
# print(cities)

# temp = 61
# if temp >= 85:
#     print(f'{temp} its a hot day!')
# elif temp <= 85 and temp >= 60:
#     print(f'{temp} its a nice day!')
# else:
#     print('its a cool day')

# def multNum(n1, n2):
#     return n1 * n2
# result = print(multNum(2,4))

# dic = {
#     'name': 'lou',
#     'age': 3,
#     'favFood': 'purina',
#     'hobby': 'birdwatching'
# }

# del dic['hobby']
# dic['age'] = 4
# dic['ishero'] = True
# print(dic)


# 🔍 Challenge: Dig into the Data
# You’ve got a list of dictionaries that represents pets and their owners:


# pets = [
#     {"owner": "Andrea", "pets": ["Louie", "Buddy"]},
#     {"owner": "Chris", "pets": ["Max"]},
#     {"owner": "Taylor", "pets": ["Bingo", "Charlie", "Milo"]}
# ]


# for record in pets:
#     owner_name = record["owner"]
#     number_of_pets = len(record["pets"])
#     print(f"{owner_name} has {number_of_pets} pets.")

# all_pets = []

# for record in pets:
#     for pet_name in record["pets"]:
#         all_pets.append(pet_name)

# print(all_pets)

# b_pets = [pet_name for record in pets for pet_name in record["pets"] if pet_name.startswith("B")]

# print(b_pets)

# Andrea has 2 pets.

# Create a list of all the pet names (just the names, one list).

# (Bonus) Use a list comprehension to create a list of just the pet names that start with "B".



# recipe_book = {
#     "Spaghetti Bolognese": {
#         "ingredients": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic"],
#         "instructions": "Cook spaghetti. In a pan, sauté onions and garlic. Add ground beef and tomato sauce. Simmer and serve over pasta.",
#         "prep_time": 30,  # in minutes
#         "difficulty": "medium"
#     },
#     "Grilled Cheese": {
#         "ingredients": ["bread", "butter", "cheese"],
#         "instructions": "Butter bread, place cheese in between. Grill on both sides until golden brown.",
#         "prep_time": 10,
#         "difficulty": "easy"
#     },
#     "Chicken Curry": {
#         "ingredients": ["chicken", "curry powder", "coconut milk", "onion", "garlic"],
#         "instructions": "Cook chicken, sauté onions and garlic. Add curry powder and coconut milk. Simmer and serve with rice.",
#         "prep_time": 45,
#         "difficulty": "hard"
#     }
# }
# print(recipe_book.get('Spaghetti Bolognese').get('ingredients'))
# print(recipe_book.get('Grilled Cheese').get('prep_time'))
# print(recipe_book.get('Chicken Curry').get("difficulty"))

# for recipe, details in recipe_book.items():
#     print(f'{recipe} is {details['difficulty']}')

# students = {
#     "Alice": {
#         "math": 90,
#         "science": 85,
#         "english": 92,
#         "history": 88
#     },
#     "Bob": {
#         "math": 75,
#         "science": 80,
#         "english": 78,
#         "history": 85
#     },
#     "Charlie": {
#         "math": 95,
#         "science": 88,
#         "english": 94,
#         "history": 91
#     }
# }

# alice_grades = students["Alice"]

# # Calculate the average
# average_grade = sum(alice_grades.values()) / len(alice_grades)

# # Print the result with 2 decimal places
# print(f"Alice's average grade is {average_grade:.2f}")

# employees = {
#     "John": {
#         "salary": 50000,
#         "bonus": 5000,
#         "years_at_company": 3
#     },
#     "Jane": {
#         "salary": 60000,
#         "bonus": 7000,
#         "years_at_company": 5
#     },
#     "Alice": {
#         "salary": 70000,
#         "bonus": 8000,
#         "years_at_company": 7
#     }
# }
# john_total = employees['John']
# total =john_total['salary']+ john_total['bonus']
# print(f'John salary is {total}')

# salaries = [employee['salary'] for employee in employees.values()]

# # Calculate the average salary
# averageSal = sum(salaries) / len(salaries)

# # Print the result
# print(f"The average salary is {averageSal:.2f}")


# def vowelC(str):
#     result = "aeiouAEIOU"
#     count = 0
#     for char in str:
#         if char in result:
#             count += 1
#     return count
     
# print(vowelC('hello world'))
        
# larget num in a list
# takes in a num, loops thru and finds the largest num

# def big(num):
#     result = num[0]
#     for i in num:
#         if i > result:
#             result = i
#     return result
# print(big([1,2,3,4]))

# def count_vowels(word):
#     result = 'aeiouAEIOU'
#     count = 0
#     for v in word:
#         if v in result:
#             count +=1
#     return count
# print(count_vowels('Hello World'))


# def onlyEvens(numbs):
#     result = []
#     for i in numbs:
#         if i % 2 == 0:
#             result.append(i)
#     return result
# print(onlyEvens([1,2,3,4,5,6]))     
# 
# 

# fun that takes a list of numbs
# returns the sum of the only even numbers
# we will need to loop thru it and find the evens then add them together
    

# def sumEvenNums(nums):
#     sum = 0
#     for even in nums:
#         if even % 2 == 0:
#             sum += even
#     return sum

# print(sumEvenNums([1,2,3,4,5,6]))
    


# def sumAllN(num):

#     sum = 0
#     for i in num:
#         sum += i 
#     return sum
# print(sumAllN([1,2,3,4]))

# def sumPosN(nums):
#     sumP = 0
#     for i in nums:
#         if i > 0:
#             sumP += i
#     return sumP
# print(sumPosN([-1, 2, -3, 4]) )

# def sum_in_range(nums):
#     sum = 0
#     for numbers in nums:
#         if numbers > 5:
#             sum += numbers
#     return sum
# print(sum_in_range([1,6,3,7,2]))

# def findDupes(lst):
#     result = []
#     seen = set()  # Use a set to track seen items
#     for i in lst:
#         if i in seen:
#             if i not in result:  # Ensure each duplicate is added only once
#                 result.append(i)
#         else:
#             seen.add(i)  # Add the item to the set
#     return result

# print(findDupes([1, 2, 3, 4, 2, 3]))  # should return [2, 3]



# def dupe(list):
#     res = []
#     seen = set()
#     for i in list:
#         if i in seen:
#             if i not in res:
#                 res.append(i)
#         else:
#             seen.add(i)
#     return res
# print(dupe([1,2,1,2,3,4,5]))

# def hasD(list):
#     seen = set()
#     for i in list:
#         if i in seen:
#             return True
#         seen.add(i)
    
#     else:
#         return False
# print(hasD([1,2,3,4,2]))

# def strR(str):
#     return str[::-1]
# print(strR('hello'))

# def odd_sum(nums):
#     total = 0
#     for odd in nums:
#         if odd % 2 != 0:
#             total += odd
#     return total
# print(odd_sum([1,2,3,4,5]))

# def square_evens(numbers):
#     sq = 0
#     newList = []
#     for even in numbers:
#         if even % 2 == 0:
#             newList.append(even * even)
#     return newList
# print(square_evens([1, 2, 3, 4, 5, 6]))


# def count_word_frequencies(word_list):
#     word_counts = {}
#     # your loop here
#     for words in word_list:
#         if words in word_counts:
#             word_counts[words] += 1
#         else:
#             word_counts[words] = 1
#     return word_counts

# print(count_word_frequencies('hello'))
# print(count_word_frequencies(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))

# def count_evens(nums):
#     count = 0
#     for even in nums:
#         if even % 2 == 0:
#             count += 1
#     return count
# print(count_evens([1,2,3,4,5]))


        
