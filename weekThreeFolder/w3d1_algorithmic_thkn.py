

# PROBLEM: Find the max value in a list of numbers.
# Example Problem: Finding the Maximum Value

# Understand the Problem
#     Input: List of Numbers
#     Output: The largest number in the list
#     Constraint: The list has at least one number

# Devise a Plan 
#     Initalize a variable to track the max Val
#     Check each number in the list
#     If a num is larger than our current max, update the max
#     After checking all nums, return the max

# Implement the Solution(Pseudocode)

# def findMax(nums):
#     maxV = nums[0]
#     for num in nums:
#         if num > maxV:
#             max = num
   
#     return maxV

# print(findMax([2,3,5,66,7,5,22]))
# print(findMax([-10,22,-2]))
# print(findMax([42]))



# convert f to c or c to f:
# input: numbers
# input('Enter temp in Celsius: ')
# input('Enter temp in Fahrenheit: ')

# output: the number converted to f or c/ display result
# print(f'The temp in Fahreneit is: {fahrenheit}')
# print(f'The temp in Celsius is: {celsius} ')

# constraint: The input must be a valid number (integer or decimal) can you
#  a try except to make sure input is valid

# Provide Clothing Advice based on temp

# to get f to c  celsuius 
# (fahrenheit - 32) * 5 / 9

# to get c to f  fahrenheit 
# (celsuius * 9 / 5) + 32


# example of 0(n)

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1


# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     raise ValueError(f'Target {target} not found in the array')

# arr = [5,8,2,9]
# print(linear_search(arr,2))
# print(linear_search(arr,7))


# example of 0(log n)

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# arr = [1,3,5,7,9,11]
# print(binary_search(arr, 7))
# print(binary_search(arr, 8))


# Breakout Room Instructions

# Instructions:
# For each of the following code snippets, determine:
# The time complexity (Big O notation)
# The space complexity (Big O notation)
# Any optimization opportunities
# Discuss how each algorithm would perform with very large inputs
# Code Snippets:
# Snippet 1:

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total


#  Time Complexity:
# O(n) — You loop through each element exactly once.
#  Space Complexity:
# O(1) — Only a few variables (total and num), no extra data structures that grow with input size.
#  Optimization Opportunities:
# This is already efficient (linear time and constant space). No real improvements needed.
#  How it performs with large inputs:
# It performs well even with large arrays because it only needs one pass and minimal extra memory.




# Snippet 2:
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

#  Time Complexity:
# O(n²) — A nested loop; for every element, you compare it to every other element after it.
# Space Complexity:
# O(d) — Where d is the number of duplicate elements found (stored in duplicates list).
#  Optimization Opportunities:
# You could improve this to O(n) time using a set to track seen elements:




# Snippet 3:
def first_and_last(arr, target):
    first = -1
    last = -1
    
    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i
    
    return [first, last]


#  Time Complexity:
# O(n) — Single pass through the list.
# Space Complexity:
# O(1) — Only fixed variables (first, last), not growing with input size.
# Optimization Opportunities:
# Already efficient for unsorted arrays.
# If the array were sorted, you could use binary search to find first and last separately in O(log n) time.
#  How it performs with large inputs:
# Performs well for unsorted data (linear time is acceptable).
# Could be faster (logarithmic) with sorted data and binary search.

















