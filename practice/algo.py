# # Problem:
# # Given a list of integers, return a new list containing only the even numbers from the original list, in the same order.
# # Input: [1, 2, 3, 4, 5, 6]
# # Output: [2, 4, 6]
# # Hints for solving:
# # You’ll need a loop to go through each number.
# # Use the modulus operator (%) to check if a number is even.
# # Append matching numbers to a new list.
# def get_evens(listOfNums):
#     result = []
#     for num in listOfNums:
#         if num % 2 == 0:
#             result.append(num)
    
#     return result
# print(get_evens([1,2,3,4,5,6]))





# # Problem:
# # Given a list of integers, return a new list containing the squares of only the odd numbers, in the same order.
# # Input: [1, 2, 3, 4, 5]
# # Output: [1, 9, 25]
# # Hints:
# def get_odd_sq(listOfN):
#     result = []
# # Loop through the list.
#     for num in listOfN:
# # Use % to check if a number is odd (num % 2 != 0).
#         if num % 2 != 0:
#             result.append(num ** 2)
# # Square an odd number with num ** 2.
#     return result
# # Append to your new list.
# print(get_odd_sq([1,2,3,4,5]))





# # Problem:
# # Given a list of integers, return the sum of all the even numbers in the list.
# # Example:
# # Input: [1, 2, 3, 4, 5, 6]  
# # Output: 12   # (2 + 4 + 6)
# # Hints:
# def sum_of_evens(listOfN):
#     total = 0
# # Loop through the list.
#     for num in listOfN:
#         if num % 2 == 0:
#             total += num
# # Use % to check if a number is even.
#     return total
# # Keep a running total in a variable instead of appending to a list.
# print(sum_of_evens([1,2,3,4,5,6]))
       




# # Problem:
# # Given a list of integers, return the sum of the squares of all the odd numbers in the list.
# # Example:
# # Input: [1, 2, 3, 4, 5]  
# # Output: 35   # (1² + 3² + 5² = 1 + 9 + 25)
# def sum_of_sq(listOfN):
#     sum = 0
# # Loop through the list.
#     for num in listOfN:
#         if num % 2 != 0:
#             sum += (num ** 2)
# # Check if a number is odd (num % 2 != 0).
#     return sum
# # Square it (num ** 2).
# print(sum_of_sq([1,2,3,4,5]))
# # Keep a running total instead of a list.




# # Problem:
# # Given a list of integers, return two results:
# # The sum of all even numbers.
# # The sum of all odd numbers.
# # Return them as a tuple in the form (even_sum, odd_sum).
# # Example:
# # Input: [1, 2, 3, 4, 5, 6]  
# # Output: (12, 9)   # Even sum = 2+4+6 = 12, Odd sum = 1+3+5 = 9
# # Hints:
# def two_sum_tup(listOfN):

#     even_sum = 0
#     odd_sum = 0

#     for num in listOfN:
#         if num % 2 == 0:
#             even_sum += num
# # Use two variables (even_sum and odd_sum).
#         else:
#             odd_sum += num
# # Loop through the list once.
#     return even_sum, odd_sum
# # Check if each number is even or odd.
# print(two_sum_tup([1,2,3,4,5,6]))
# # Add to the correct total.





# # Problem:
# # Given a list of integers, return a tuple containing:
# # The largest even number in the list.
# # The smallest odd number in the list.
# # If there are no even numbers, use None for the largest even.
# # If there are no odd numbers, use None for the smallest odd.
# # Input: [1, 2, 3, 4, 5, 6]  
# # Output: (6, 1)
# # Hints:
# def large_and_small(listOfN):
#     largest_even = None
#     smallest_odd = None
# # You can start largest_even as None and smallest_odd as None.
# # Loop through the list once.
#     for num in listOfN:
#         if num % 2 == 0:
#             if largest_even is None or num > largest_even:
#                 largest_even = num
# # For each number:
#         else:
#            if smallest_odd is None or num < smallest_odd:
#                smallest_odd = num
# # If it’s even, update largest_even if it’s None or bigger than the current.
#     return largest_even, smallest_odd
# # If it’s odd, update smallest_odd if it’s None or smaller than the current.
# print(large_and_small([1,2,3,4,5,6]))





# Problem:
# Given a list of integers, return a new list containing only the numbers that are greater than the average of the list.

# Input: [1, 2, 3, 4, 5, 6]  
# Average: 3.5  
# Output: [4, 5, 6]
# Hints:

# First, calculate the average (sum(nums) / len(nums)).
# def get_greater_than_avg(listOfN):
#     avg = (sum(listOfN)/len(listOfN))
#     newList = []
# # Loop through the list.
#     for num in listOfN:
#         if num > avg:
#             newList.append(num)
#     return newList
# # Append numbers that are greater than the average to a new list.
# print(get_greater_than_avg([1,2,3,4,5,6]))
# # Return that new list.





# Problem:
# Given a list of integers, return a tuple containing:
# The count of numbers greater than the average.
# The count of numbers less than or equal to the average.

# Example:
# Input: [1, 2, 3, 4, 5, 6]  
# Average: 3.5  
# Output: (3, 3)  # 3 numbers > avg, 3 numbers <= avg
# Hints:
def two_counts(listOfN):
    avg = (sum(listOfN)/len(listOfN))
# Calculate the average first.
    counter_1 = 0
    counter_2 = 0
# Create two counters starting at 0.
    for num in listOfN:
        if num > avg:
            counter_1 += 1
        else:
            counter_2 += 1
    return counter_1, counter_2
# Loop through the list and update the correct counter.
print(two_counts([1,2,3,4,5,6]))
# Return the two counts as a tuple.        






            
        
            