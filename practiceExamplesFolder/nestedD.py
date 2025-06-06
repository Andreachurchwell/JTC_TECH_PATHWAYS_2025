# expenses = [
#     {'name': 'Rent', 'amount': 1200},
#     {'name': 'Groceries', 'amount': 300},
#     {'name': 'Utilities', 'amount': 150}
# ]

# # Task: Write code to sum all the 'amount' values
# total = 0
# for expense in expenses:
#     total += expense['amount']

# print("Total expenses:", total)  # Expected: 1650
# # Task: Print the dictionary with the highest 'amount'

# highest = expenses[0]
# for expense in expenses:
#     if expense['amount'] > highest['amount']:
#         highest = expense

# print("Highest expense:", highest)  
# # Expected: {'name': 'Rent', 'amount': 1200}
# # Task: Print expenses where the amount is greater than 200

# filtered = []
# for expense in expenses:
#     if expense['amount'] > 200:
#         filtered.append(expense)

# print("Expenses over 200:", filtered)
# # Expected: [{'name': 'Rent', 'amount': 1200}, {'name': 'Groceries', 'amount': 300}]




# expenses = [
#     {'name': 'Rent', 'amount': 1200},
#     {'name': 'Groceries', 'amount': 300},
#     {'name': 'Utilities', 'amount': 150},
#     {'name': 'Streaming', 'amount': 25},
#     {'name': 'Snacks', 'amount': 80}
# ]

# how many expenses are over a 100
# total = []
# for item in expenses:
#     if item['amount'] > 100:
#         total.append(item)
#     # print("item", item)
# print("Number of expenses over $100:", len(total))  # Should print: 3 
# result = []
# for expense in expenses:
#     if expense['amount'] < 200:
#         result.append(expense['name'])
# print(result)

# find toatl amount spent on exp that have a name longer than 7 chars


# total = 0
# for expense in expenses:
#     if len(expense['name']) > 7:
#         total += expense['amount']
# print(total)

# expenses = [
#     {'name': 'Rent', 'amount': 1200},
#     {'name': 'Groceries', 'amount': 300},
#     {'name': 'Utilities', 'amount': 150},
#     {'name': 'Streaming', 'amount': 25},
#     {'name': 'Snacks', 'amount': 80}
# ]

# highestAmount = 0
# for item in expenses:
#     if item['amount'] > highestAmount:
#         highestAmount = item['amount']
#         print(item['name'])
# print(highestAmount)

# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
# my_dict['profession'] = 'Doctor'
# print(f"Updated dictionary after adding 'profession': {my_dict}")
# # Modify Value
# my_dict['age'] = 40
# print(f"Updated dictionary after modification: {my_dict}")

# # print key
# print('City:', my_dict['city'])

# del my_dict['profession']
# print(my_dict)

# for key,value in my_dict.items():
#     print(f'{key}:{value}')

# def check_key_exists(dictionary, key_to_check):
#   return key_to_check in dictionary

# key1 = 'age'
# print(f"Does '{key1}' exist? {check_key_exists(my_dict, key1)}")

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# res_dict = dict(zip(keys, values))
# print(res_dict)


# # empty dictionary
# res_dict = dict()

# for i in range(len(keys)):
#     res_dict.update({keys[i]: values[i]})
# print(res_dict)

# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
# print(f"dictionary: {my_dict}")

# my_dict.clear()
# print(f"dictionary after removing all items: {my_dict}")

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = {**dict1, **dict2}
# print(dict3)

# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)


# def count_char_frequencies(input_string):
#   frequency_dict = {}
#   for char in input_string:
#     # Use get() method: if char is in dict, get its value; otherwise, default to 0
#     frequency_dict[char] = frequency_dict.get(char, 0) + 1
#   return frequency_dict

# string1 = 'Jessa'
# print(f"Frequencies for '{string1}': {count_char_frequencies(string1)}")

# data = {'person': {'name': 'Alice', 'age': 30}}
# print(data['person']['age'])

# students = {
#     "Alice": {"math": 85, "science": 92},
#     "Bob": {"math": 78, "science": 88},
#     "Charlie": {"math": 93, "science": 85}
# }

# for name in students:
#     scores = students[name].values()
#     average = sum(scores) / len(scores)
#     print(f"{name}'s average score is {average}")


# person = {
#     "name": "Andrea",
#     "age": 43,
#     "job": "Developer"
# }
# print(person['name'],person['job'])

# my_info = {
#     "pet": "Louie",
#     "hobby": "coding",
#     "favorite_color": "blue"
# }

# # Print just your pet's name here:
# print(my_info['pet'])
# my_info['fav_snack'] = 'fruitables'
# print(my_info)
# del my_info["hobby"]
# print(my_info)

# for key, value in my_info.items():
#     print(f"{key}: {value}")

# Your dictionary
# my_info = {
#     "pet": "Louie",
#     "hobby": "coding",
#     "fav snack": "fruitables"
# }

# # Check if "favorite_color" exists, and print its value if it does.
# # If not, print "No favorite color set."
# print(my_info.get("favorite_color", "No favorite color set."))

# def revStr(str):
#     result = ''
#     for item in str:
#         return str[::-1]
# print(revStr('my name is jessa'))



# def evenList(nums):
#     newList = []
#     for i in nums:
#         if i % 2 == 0:
#             newList.append(i)
#     return newList
# print(evenList([1,2,3,4,5]))

# def oddLisst(nums):
#     result = []
#     for i in nums:
#         if i % 2 != 0:
#             result.append(i)
#     return result
# print(oddLisst([1,2,3,4,5]))

# def sumNum(nums):
#     sum = 0
#     for i in nums:
#         sum += i 
#     return sum
# print(sumNum([1,2,3]))


# fruit_stock = {
#     "apple": 5,
#     "banana": 2,
#     "orange": 8,
#     "grape": 0
# }

# def instock(fruit_stock):
#     for i in fruit_stock:
#         if fruit_stock[i] > 0:
#             print(i)
# instock(fruit_stock)


# fruit_stock['kiwi'] = 4
# print(fruit_stock)
# fruit_stock['banana'] = 5
# print(fruit_stock)

# def grade_class(score):
#     if score >= 90:
#         return 'A'
#     elif score >= 80:
#         return 'B'
#     elif score >= 70:
#         return 'C'
#     elif score >= 60:
#         return 'D'
#     else:
#         return 'F'
# print(grade_class(84))

# def posOrneg(num):
#     if num >= 0:
#         return 'pos'
#     elif num == 0:
#         return 'zero'
#     else:
#         return 'neg'
# print(posOrneg(-3))


# def isPal(word):
 
#     if word[::-1].lower() == word.lower():
#         return 'yes'
#     else:
#         return 'no'
# print(isPal('racecar'))
# print(isPal('Racecar'))


# def maxNum(nums):
#     largest = nums[0]
#     for i in nums:
#         if i > largest:
#             largest = i
#     return largest
# print(maxNum([1,12,3,4,5]))

# def vCount(s):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for vowel in s:
#         if vowel in vowels:
#             count += 1
        
#     return count
# print(vCount("hello world"))
        
# def revList(lst):
#     newList = []
#     for i in range(len(lst)-1,-1,-1):
#         newList.append(lst[i])
#     return newList

# print(revList([1,2,3,4]))



# cw takes in a str sent, returns the numb of words 
# i will need a counter and i will need to loop thru the string sent. 
# somehow i will need to do split at white space and will need to return the count also use len count words

# def countWords(sent):
#     numbOfw = sent.split()
#     return len(numbOfw)
# print(countWords('hey, my name is andrea'))


# student = {
#     "name": "Andrea",
#     "grades": {
#         "math": 88,
#         "science": 92,
#         "english": 85
#     }
# }

# def getGrade(student, subject):
#     return student['grades'][subject]
# print(getGrade(student, 'science'))
    




# students = {
#     "John": {"math": 85, "science": 92},
#     "Emily": {"math": 78, "science": 88},
#     "Michael": {"math": 90, "science": 94}
# }


# # print(students["Michael"]['science'])
# students.update({"Sarah": {"math": 82, "science": 89}})
# print(students)

# def getavg(students):
#     total = 0
#     count = 0
#     for student in students:
#         total += students[student]['math']
#         count += 1
#     avg = total / count
#     print("Average math score:", avg)
# getavg(students)




# students = {
#     "John": {"math": 85, "science": 92},
#     "Emily": {"math": 78, "science": 88},
#     "Michael": {"math": 90, "science": 94}
# }

# def getavg(students):

#     for student in students:
#         print(student)
#         grades = students[student]
#         math = grades['math']
#         science = grades['science']
#         avg = (math + science)/2
#         print(f"{student}'s avg grade is {avg:.2f}")
    


# getavg(students)



students = {
    "John": {"math": 85, "science": 92, "english": 78},
    "Emily": {"math": 78, "science": 88, "english": 90},
    "Michael": {"math": 90, "science": 94, "english": 85}
}

def getavg(students):
    for student, grades in students.items():
        total = sum(grades.values())
        count = len(grades)
        avg = total / count
        print(f"{student}'s average grade is {avg:.2f}")

getavg(students)
