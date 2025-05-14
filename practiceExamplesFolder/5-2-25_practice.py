# # 🧪 Practice Task: "Movie Filter"
# # Scenario:
# # You’re given a list of movies. Each movie is represented by a dictionary with the following keys:

# # "title" (string)

# # "year" (int)

# # "rating" (float)

# # Your Task:
# # Write a Python program that:

# # Filters and returns only the movies released after a given year and with a rating above a given threshold.

# # Sorts the result by rating (highest first).

# # Prints the titles of the filtered and sorted movies.

# movies = [
#     {"title": "Inception", "year": 2010, "rating": 8.8},
#     {"title": "The Matrix", "year": 1999, "rating": 8.7},
#     {"title": "Interstellar", "year": 2014, "rating": 8.6},
#     {"title": "The Flash", "year": 2023, "rating": 6.8},
#     {"title": "The Batman", "year": 2022, "rating": 7.9},
#     {"title": "Oppenheimer", "year": 2023, "rating": 8.4},
# ]

# def filter_movies(movies, min_year, min_rating):
#     print('min_year==', min_year)
#     print('min_rating=', min_rating)
#     result = []
#     for movie in movies:
#         print('movie=', movie)
#         if movie['rating'] > min_rating and movie['year'] > min_year:
#             result.append(movie)
#     return result

# filter_movies(movies, 2010,8.0)
# filtered = filter_movies(movies, 2010, 8.0)
# print(filtered)
# 🧠 Task 1: Check if a Number is Positive, Negative, or Zero
# Write a function that checks whether a number is positive, negative, or zero. Here’s the flow:

# If the number is greater than 0, print "Positive".

# If it’s less than 0, print "Negative".

# If it’s equal to 0, print "Zero".

# def checker(nums):
#     results = []  # Create a list to store the results
#     for num in nums:
#         if num == 0:
#             results.append('its zero')
#         elif num < 0:
#             results.append('neg')
#         else:
#             results.append('pos')
#     return results  # Return the list of results

# print(checker([1, 2, 3, 0, -1]))

# 🧠 Task 2: Find the Maximum Number in a List
# Write a function that finds the maximum number in a list of numbers. You need to:

# Initialize a variable that will hold the maximum value.

# Loop through the list of numbers.

# For each number, check if it’s larger than the current "maximum."

# If it is, update the maximum variable with that number.

# Once the loop finishes, return the maximum number.

# def maxNum(nums):
#     current_max = nums[0]  # Initialize with the first number in the list
#     for num in nums:
#         if num > current_max:
#             current_max = num  # Update current_max if a larger number is found
#     return current_max

# print(maxNum([1, 2, 3, 4, 5]))

# 🧠 Task 3: Count Occurrences of Each Element
# Write a function that counts how many times each element appears in a list. For example, 
# given a list [1, 2, 2, 3, 3, 3], your function should return a dictionary like this: {1: 1, 2: 2, 3: 3}.

# def occur(lofN):
#     countStore = {}
#     for i in lofN:
#         if i in countStore:
#             countStore[i] += 1
#         else:
#             countStore[i] = 1
#     return countStore
# print(occur([1, 2, 3, 4, 4, 4, 4]))


# def printItems(listOfItems):
#     index = 0
#     for item in listOfItems:
#         print(item, index)
#         index += 1
# printItems(["apple", "banana", "cherry"])

# def evenOrOdd(num):
#     if num % 2 == 0:
#         return 'its even'
#     else:
#         return 'its odd'
    
# print(evenOrOdd(4))


# def countOcc(listOfN, target):
#     count = 0
#     for num in listOfN:
#         print(num)
#         if num == target:

#             count += 1

#     return count
# print(countOcc([1,2,3,4,5],2))

# def sumlist(nums):
#     sum = 0
#     for num in nums:
#         if num % 2 == 0:
#             sum += num
#     return sum
# print(sumlist([1,2,3,4]))

# def findMin(nums):
#     minNum = nums[0]
#     for num in nums:
#         if num < minNum:
#             minNum = num
#     return minNum

# print(findMin([1,2,3,4]))

# def revList(listOfNums):
#     newList = []
#     for item in listOfNums[::-1]:  # Loop through the list in reverse order
#         newList.append(item)  # Append each item to newList
#     return newList

# print(revList([1, 2, 3, 4]))  # Should output: [4, 3, 2, 1]


# def revAstr(str):
#     result = ''
#     for i in str:
#         print('i==',i)
#         result = i + result
#     return result
# print(revAstr('hello'))

# def countEs(nums):
#     count = 0
#     for num in nums:
#         if num % 2 == 0:
#             count += 1
#     return count

# print(countEs([1,2,3,4,5]))

# def findMax(nums):
#     maxNum = nums[0]
#     for num in nums:
#         if num > maxNum:
#             maxNum = num
#     return maxNum



# print(findMax([1,2,3,4,5]))

# def sumOfNum(nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum

# print(sumOfNum([1,2,3]))


# def countOccurrences(li, num):
#     count = 0
#     for item in li:
#         if item == num:
#             count += 1
#     return count
# print(countOccurrences([1,1,2,3], 1))


# def isPalindrome(listOfsomething):
#     if listOfsomething == listOfsomething[::-1]:
#         return True
#     else:
#         return False
# print(isPalindrome([1,2,3,3,2,1]))   
# 
# def mergeDicts(dic1, dic2):
#     # Create a copy of dic1 to avoid modifying the original
#     merged_dict = dic1.copy()
    
#     # Update merged_dict with the contents of dic2
#     merged_dict.update(dic2)
    
#     # Return the merged dictionary
#     return merged_dict

# # Test the function
# print(mergeDicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

# def transStr(str):
#     replStr = ''
#     for vowel in str:
#         if vowel in 'aeiouAEIOU':
#             replStr += '*'
#         else:
#             replStr += vowel.upper()
#     return replStr
# print(transStr('andrea'))

# def sortBySecond(lst):
#     return sorted(lst, key= lambda x:x[1])
# print(sortBySecond([(1,3), (2,2),(4,1)]))
# sorted_list = sorted([(1, 3), (2, 2), (4, 1)], key=lambda x: x[1])
# lst = [(1, 3), (2, 2), (4, 1)]
# sorted_lst = sorted(lst, key=lambda x: x[1])  # Sorting based on the second element
# print(sorted_lst)

# Problem: Count Occurrences of an Element in a List
# Task:
# Given a list of integers nums, count how many times a specific number appears in the list.  

# def countOcc(nums, target):
#     count = 0
#     for num in nums:
#         if num == target:
#             count +=1
#     return count
# nums = [1, 2, 3, 4, 1, 2, 1]
# target = 1
# print(countOcc(nums,target)) 

# def counttwos(nums,target):
#     count = 0
#     for num in nums:
#         if num == 2:
#             count +=1
#     return count
# nums = [5, 2, 3, 2, 2, 8, 5]
# target = 2
# print(counttwos(nums, target))


# def revAstr(s):
#     return s[::-1]
# s = 'hello'
# print(revAstr(s))

# def twoS(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
#     return []


# nums = [2, 7, 11, 15]
# target = 9
# print(twoS(nums, target))


# def sumOfallNums(nums):
#     sum = 0
#     for num in nums:
#         sum = sum + num
#     return sum
# print(sumOfallNums([1,2,3,4,5]))



# def countEvens(nums):
#     countE = 0
#     for num in nums:
#         if num % 2 == 0:
#             countE = countE + 1
#     return countE
# print(countEvens([1,2,3,4,5]))

# def isPal(s):  # This is the function that takes a string as input
#     for i in range(len(s) // 2):  # Loop through the first half of the string
#         # Compare the character at position i (from the start) with the character at position len(s) - 1 - i (from the end)
#         if s[i] != s[len(s) - 1 - i]:
#             return False  # If the characters don't match, return False (it's not a palindrome)
    
#     return True  # If all characters match, return True (it's a palindrome)

        
# def combine_lists(lst1, lst2):
#     return lst1 + lst2
# lst1 = [1,2,3]
# lst2 = [4,5,6]
# print(combine_lists(lst1,lst2))

# def removeEvens(lst):
#     newLst = []
#     for num in lst:
#         if num % 2 != 0:
#             newLst.append(num)
#     return newLst

# lst = [1,2,3,4,5,6,7]
# print(removeEvens(lst))

# def largest_odd(nums):
#     maxOdd = None
#     for item in nums:
#         if item % 2 != 0:
#             if maxOdd is None or item > maxOdd:
#                 maxOdd = item

#     return maxOdd

# nums = [10,22,5,3,8,13]
# print(largest_odd(nums))

# def smallestEven(nums):
#     smallE = None
#     for item in nums:
#         if item %2==0:
#             if smallE is None or item < smallE:
#                 smallE = item
#     return smallE
# nums = [10,22,5,3,8,13]
# print(smallestEven(nums))

# def filter_by_len(words, length):
#     newLst = []
#     for word in words:
#         if len(word) > length:
#             newLst.append(word)
#     return newLst
# words = ["apple", "pie", "banana", "cat", "elephant"]
# length = 4
# print(filter_by_len(words, length))






    

           

    

