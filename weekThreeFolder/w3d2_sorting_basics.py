# BUBBLE SORT  

# this is good for smaller data sets

# def bubbleSort(myList):
#     for i in range (0, len(myList) -1):
#         for j in range(0, len(myList) - 1 - i):
#             if myList[j] > myList[j + 1]:
#                 myList[j], myList[j + 1] = myList[j + 1], myList[j]
#     return myList

# theList = ['v', 'd', 'c', 'w', 'a']
# print('bubblesort===',bubbleSort(theList))





# another example of bubble sort
# def bubble_sort(arr):
#     n = len(arr)
#     # Traverse through all array elements
#     for i in range(n):
#         # Flag to optimize if no swaps occur
#         swapped = False
        
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
#             # Traverse the array from 0 to n-i-1
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
        
#         # If no swapping occurred in this pass, array is sorted
#         if not swapped:
#             break
    
#     return arr

# my_list = [6,9,3,1,34,9,76]
# print('bubblesort==' ,bubble_sort(my_list))




# # Example of O(n^2)
# def bubble_sort2(arrArray):
#     # Get the length of the array to determine how many passes we need
#     newList = len(arrArray)
    
#     # Outer loop: each pass will place the largest unsorted element at the end
#     # We need at most n passes for an array of size n
#     for indice in range(newList):
#         # Inner loop: compare adjacent elements and swap if they're in the wrong order
#         # With each pass, we can reduce the number of comparisons since the largest elements
#         # are already in their correct positions at the end
#         for subList in range(0, newList-indice-1):
#             # Compare adjacent elements
#             if arrArray[subList] > arrArray[subList+1]:
#                 # Swap the elements if they are in the wrong order
#                 # This gradually "bubbles up" larger elements to the end of the array
#                 arrArray[subList], arrArray[subList+1] = arrArray[subList+1], arrArray[subList]
    
#     # Return the sorted array
#     return arrArray

# arrArray = [23,464,565,2323,23,4,5,7]
# print('bubblesort2==' ,bubble_sort2(arrArray))




# def bubble_sorting(arr):
#     n = len(arr)
#     comparisons = 0
#     swaps = 0
    
#     for i in range(n):
#         # Track if any swap happens in this pass
#         swapped = False
#         for j in range(0, n - i - 1):
#             comparisons += 1
#             if arr[j] > arr[j + 1]:
#                 # Swap
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swaps += 1
#                 swapped = True
#             print(f"Step {comparisons}: {arr}")
#         if not swapped:
#             break  # Optimization: stop early if already sorted
#     return arr, comparisons, swaps
# arr = [64,34,25,12,22,11,90]
# print(bubble_sorting(arr))




# SELECTION SORT
# NUMBER OF SWAPS IS MUCH LOWER THAN BUBBLE 

# def selectionSort(list_a):
#     indexLen = range(0, len(list_a) -1)

#     for i in indexLen:
#         minVal = i

#         for j in range(i + 1, len(list_a)):
#             if list_a[j] < list_a[minVal]:
#                 minVal = j

#         if minVal != i:
#             list_a[minVal], list_a[i] = list_a[i], list_a[minVal]

#     return list_a

# print('selectionSort===' ,selectionSort([4,7,3,2,8,45,32,56]))






# def selection_sort(arr):
#     n = len(arr)
    
#     # Traverse through all array elements
#     for i in range(n):
#         # Find the minimum element in remaining unsorted array
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
        
#         # Swap the found minimum element with the first element
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
#     return arr




# def selection_sort(numbers):
#     length = len(numbers)
    
#     # Go through each position in the list
#     for current_position in range(length):
#         # Assume the smallest number is at the current position
#         smallest_position = current_position
        
#         # Look for a smaller number in the rest of the list
#         for next_position in range(current_position + 1, length):
#             if numbers[next_position] < numbers[smallest_position]:
#                 smallest_position = next_position
        
#         # Swap the smallest number found with the number at the current position
#         numbers[current_position], numbers[smallest_position] = numbers[smallest_position], numbers[current_position]
    
#     return numbers



# INSERTION SORT 

def insertSort(listA):
    indexL = range(1, len(listA))
    for i in indexL:
        valToSort = listA[i]

        while listA[i-1] > valToSort and i > 0:
            listA[i], listA[i-1] = listA[i-1], listA[i]

            i = i -1
    return listA

print('insertSort===',insertSort([4,6,7,34,43,77,22,11,9]))


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    
    return arr