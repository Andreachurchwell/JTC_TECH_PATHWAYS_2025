# Problem: Find the sum of all even numbers in a list.
# Example Input:
# [1, 2, 3, 4, 5, 6]

# Example Output:
# 12 (because 2 + 4 + 6 = 12)

# Try solving this by iterating over the list and checking if each number is even. Once you have your approach, let me know, and we’ll walk through it together!

# def sumOfEven(listOfN):
#     # result = []
#     sum = 0
#     for nums in listOfN:
#         if nums % 2 == 0:
#             sum += nums
#     return sum
# print(sumOfEven([1,2,3,4]))

# def countOfEven(listOfN):
#     # result = []
#     count = 0
#     for nums in listOfN:
#         if nums % 2 == 0:
#             count += 1
#     return count
# print(countOfEven([1,2,3,4]))


# def returnOfEven(listOfN):
#     myList = []
#     for num in listOfN:
#         if num % 2 == 0:
#             myList.append(num)
#     return myList
        

# print(returnOfEven([1,2,3,4]))

# Problem: Count the number of vowels in a string.
# Example Input:
# "hello world"

# Example Output:
# 3 (because it has e, o, and o)

# def vowelCount(strOfwords):
#     count = 0
#     for letter in strOfwords:
#         if letter in 'aeiouAEIOU':
#             count += 1
#     return count
# print(vowelCount('Hello World'))


# Problem: Word Frequency Counter
# Write a function that takes a list of words and returns a dictionary 
# where the keys are the words, and the values are how many times each word appears.

# Example Input:
# ["apple", "banana", "apple", "orange", "banana", "apple"]

# Example Output:
# {"apple": 3, "banana": 2, "orange": 1}

# def wordFcounter(listOfwords):
#     result = {}
    
#     for word in listOfwords:
#         if word in result:
#             result[word] += 1
#         else:
#             result[word] = 1
#     return result

# print(wordFcounter(["apple", "banana", "apple", "orange", "banana", "apple"]))


# Problem: Remove all vowels from a string.
# Write a function that takes a string and removes all the vowels (a, e, i, o, u in both uppercase and lowercase).

# Example Input:
# "hello world"

# Example Output:
# "hll wrld"

# def removeVs(strOfwords):
#     resultStr = ''
#     for word in strOfwords:
#         if word not in 'aeiouAEIOU':
#             resultStr += word
#     return resultStr
# print(removeVs('Hello World'))


# Write a function that takes a list of words and returns a 
# single string with the words in reverse order, separated by spaces.

# Example Input:

# word = ["hello", "world", "python"]

# Example Output:
# "python world hello"
# def singleStr(listOfw):
#     result = ''
#     for word in listOfw[::-1]:
#         print(word)
#         result += word + ' '
#     return result

# print(singleStr(["hello", "world", "python"]))

# Problem: Find the longest word in a list and return its length.
# Write a function that takes a list of words and returns the length of the longest word.


# def longword(listwords):
#     maxL = 0
#     for word in listwords:
#         if len(word)> maxL:
#             maxL = len(word)
#     return maxL

# print(longword(['apple', 'banana', 'grape','kiwi']))

# def countOcc(listOfstrs):
#     result = {}
#     for item in listOfstrs:
#         if item in result:
#             result[item] += 1
#         else:
#             result[item] = 1
#     return result
# print(countOcc(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))

# Write a function that takes a list and returns the element that appears the most. 
# If there is a tie, return any of the most frequent elements.
# this solution is wrong..never could figure it out:
# def appearMost(listOfw):
#     result = {}
#     highestVal = 0
#     for word in listOfw:
#         if word in result:

#             result[word] += 1
#             highestVal = result
#         else:
#             result[word] = 1
#     return highestVal
# print(appearMost(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))

# heres the solution ugh
# def appearMost(listOfw):
#     result = {}

#     # Step 1: Count occurrences
#     for word in listOfw:
#         if word in result:
#             result[word] += 1
#         else:
#             result[word] = 1

#     # Step 2: Find the word with the highest count
#     most_common = ''
#     max_count = 0

#     for word, count in result.items():
#         if count > max_count:
#             max_count = count
#             most_common = word

#     return most_common

# print(appearMost(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))





# 🧩 Step 1: Lists Practice
# Create a list of 5 of your favorite things (strings).

# Practice:

# Adding an item.

# Removing an item.

# Accessing the first and last items.

# Reversing the list (with slicing and a loop).
myFavs = ['louie','gardening', 'bballgames', 'shopping']
myFavs.append('foodie')
myFavs.remove('bballgames')
myFavs[0]
myFavs[-1]
print(myFavs)

def myFavList(listOffavs):
    return listOffavs[::-1]
print(myFavs)

def myFavList(listOffavs):
    result = []
    for item in listOffavs:
        result.insert(0, item)  # Adds each item to the beginning
    return result

print(myFavList(myFavs))  # Should print your favorites reversed
