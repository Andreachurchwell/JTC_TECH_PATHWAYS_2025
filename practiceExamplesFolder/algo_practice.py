# 🧠 Problem: Two Sum (Easy/Medium)

# Given a list of integers nums and a target integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Input: nums = [2, 7, 11, 15], target = 9  
# Output: [0, 1]  # Because nums[0] + nums[1] == 2 + 7 == 9

# 1. Loop through the list using index i (starting from 0 to length - 1)
# 2. Inside that loop, loop again using index j (starting from i + 1 to length)
# 3. For each pair (nums[i] and nums[j]), check if nums[i] + nums[j] equals the target
# 4. If they add up to the target:
#      - return [i, j]

# def twoSum(nums, target):

#     for i in range(len(nums)):
#         # print('i==', i)
#         for j in range(i + 1,len(nums)):
#             # print('j==', j)
#             if nums[i] + nums[j] == target:
#                 return [i,j]

# print(twoSum([2,7,11,15], 9))



# 🧠 Problem: Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets are closed by the same type of brackets.

# Open brackets are closed in the correct order.

# def isValid(s):
#     for char in s:
#         print(char)

# isValid("()[]{}")

# we have a list of nums we need to loop thru the list 
# after looping thru i think we will need another loop 
# after that we can compare and if the bigger num becomes max
# def maxnum(nums):
    
#     maxn = nums[0]
#     for i in range(len(nums)):
#         print('nums[i]', nums[i])
#         if nums[i]> maxn:
#             maxn = nums[i]
#     return maxn


# print(maxnum([1,3,6,2]))


# def smallnum(nums):
#     smallest = nums[0]
#     for num in range(len(nums)):
#         if nums[num] < smallest:
#             smallest = nums[num]
#     return smallest
# print(smallnum([3,6,8,2]))




# def isSorted(nums):
#     for i in range(len(nums)-1):
#         if nums[i] > nums[i+1]:
#             return False
#     else:
#         return True
        
# print(isSorted([1,2,3,4]))
# print(isSorted([2,6,2,4,7,1]))



# def desSort(nums):
#     for i in range(len(nums)-1):
#         if nums[i] < nums[i + 1]:
#             return False
#     else:
#          return True
# print(desSort([5,4,2,1]))
# print(desSort([1,2,34]))
# def revStr(s):
#     result = ''
#     for char in s:
#         result = char + result 
#     return result

# print(revStr('hello')) 

