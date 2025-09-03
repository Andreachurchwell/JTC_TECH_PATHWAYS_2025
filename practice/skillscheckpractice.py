# def convert_to_celsius(f_list):
#     result = []
#     for temp in f_list:
#         cel = (temp -32)* 5 / 9
#         result.append(cel)
#     return result

# print(convert_to_celsius([32, 68, 77, 104]))

# ✅ PRACTICE PROMPT: Return only even numbers
# Write a function called get_even_numbers() that:

# Takes in a list of integers

# Returns a new list with only the even numbers

# def get_even_nums(listOfInt):
#     newList = []
#     for i in listOfInt:
#         if i % 2 == 0:
#             newList.append(i)
#     return newList
        
# print(get_even_nums([1,2,3,4,5,6]))

# ✅ PRACTICE PROMPT #3: Strings & Conditionals
# Task:
# Write a function that takes a string and returns True if it’s a palindrome, and False if it’s not.
# A palindrome reads the same forward and backward (like "madam" or "racecar").


# def ispal(word):
#     rev_word = word[::-1]
#     if word == rev_word:
#         return True
#     else:
#         return False
# print(ispal('racecar'))
# print(ispal('racecardf'))

        