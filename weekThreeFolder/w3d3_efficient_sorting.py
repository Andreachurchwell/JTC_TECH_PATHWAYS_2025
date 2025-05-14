# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = [x for x in arr[1:] if x <= pivot]
#     right = [x for x in arr[1:] if x > pivot]
#     return quicksort(left) + [pivot] + quicksort(right)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = quick_sort([x for x in arr[1:] if x <= pivot])
    right = quick_sort([x for x in arr[1:] if x > pivot])
    return left + [pivot] + right

# Test array
test_arr = [5, 3, 8, 4, 2, 7, 1, 10]

# Run quick_sort
sorted_arr = quick_sort(test_arr)

print("Original:", test_arr)
print("Sorted:", sorted_arr)





def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

print(merge_sort([38,27,43,3,9,82,10]))




def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from left and right, and add the smallest one to result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from left
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from right
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)




# myList = [22, 33, 15, 101, 3, 75, 12, 15, 4, 8]

# We have an unordered list that needs sorted

# def merge_sort(arr):
#     # arr is the Array/List we will call the function on to sort.
#     if len(arr) <= 1:
#         # this reduces the list to single element
#         return arr
#     mid = len(arr) // 2
#         # the // operation automatically floors the number < Math.floor >
#     left = merge_sort(arr[:mid])
#         # first recursion
#     right = merge_sort(arr[mid:])
#         # second recursion
#     result = []
#         # empty list to contain the split items
#     leftEye = rightEye = 0
#         # enter the while loop
#     while leftEye < len(left) and rightEye < len(right):
#         if left[leftEye] < right[rightEye]:
#             result.append(left[leftEye])
#             leftEye += 1
#         else:
#             result.append(right[rightEye])
#             rightEye += 1
#     result.extend(left[leftEye:])
#     result.extend(right[rightEye:])
#     return result

# print(f" Show me the money Lebowski!!! {merge_sort(myList)}")
# [3, 4, 8, 12, 15, 15, 22, 33, 75, 101]
# # Now we can reuse this function repeatedly

# newArray = [301, 1982, 158, 23, 15, 42, 777, 369, 4]

# print(f" Make my merge... {merge_sort(newArray)}")
# [4, 15, 23, 42, 158, 301, 369, 777, 1982]
# ### Hold for Applause ###


dogs = [
    {"name": "Louie", "age": 5},
    {"name": "Bella", "age": 2},
    {"name": "Charlie", "age": 3}
]
def merge_sort2(arr, key):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort2(arr[:mid], key)
    right = merge_sort2(arr[mid:], key)
    return merge2(left, right, key)

def merge2(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
sorted_dogs = merge_sort2(dogs, key="age")
print(sorted_dogs)
