# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Found target at index i
#     return -1  # Target not found
# nums = [4, 2, 7, 1, 9]
# print(linear_search(nums, 7))  






# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2  # Find the midpoint
#         if arr[mid] == target:
#             return mid  # Found the target
#         elif arr[mid] < target:
#             left = mid + 1  # Search in the right half
#         else:
#             right = mid - 1  # Search in the left half
#     return -1  # Target not found
# nums = [1, 2, 4, 7, 9]
# print(binary_search(nums, 7))  # Output: 3






# Breakout Room #1
## Coupon Code Problem

# list of valid coupon codes and the corresponding discount amounts (unsorted)
# gift_cards = [
#     {"code": "XFD890", "discount": 15},
#     {"code": "JLK321", "discount": 20},
#     {"code": "ABC123", "discount": 10},
#     {"code": "ZZZ999", "discount": 25}
# ]


# # create a function that takes a coupon code and returns the discount amount or None if the code is not valid

# def check_coupon(coupon_code):
#     for cc in gift_cards:
#         # print('cc==', cc)
#         if cc['code'] == coupon_code:
#             return f'Coupon {cc['discount']}% off!!'
#     return None



# # user input coupon code
# coupon_code = input("Enter your coupon code: ")
# print(check_coupon(coupon_code))






# Binary Search Breakout Session

## Coupon Code Problem (Sorted List)

# list of valid coupon codes and the corresponding discount amounts (sorted by code)
gift_cards = [
    {"code": "ABC123", "discount": 10},
    {"code": "BXY456", "discount": 30},
    {"code": "CDE789", "discount": 12},
    {"code": "FGH012", "discount": 18},
    {"code": "IJK345", "discount": 22},
    {"code": "JLK321", "discount": 20},
    {"code": "MNO678", "discount": 28},
    {"code": "PQR901", "discount": 14},
    {"code": "STU234", "discount": 16},
    {"code": "VWX567", "discount": 24},
    {"code": "XFD890", "discount": 15},
    {"code": "YZA123", "discount": 19},
    {"code": "ZZZ999", "discount": 25}
]


# create a function that takes a coupon code and returns the discount amount or None if the code is not valid

def check_coupon_binary(coupon_code):
    left = 0
    right = len(gift_cards)
    while left <= right:
        mid = (left + right) // 2
        middleCode = gift_cards[mid]['code']

        if middleCode == coupon_code:
            return f'{coupon_code} gets {gift_cards[mid]['discount']}% off!!'
        
        elif coupon_code < middleCode:
            right = mid - 1
        else:
            left = mid + 1

    return 'Invailid coupon code..'

    


# user input coupon code
coupon_code = input("Enter your coupon code: ")
print(check_coupon_binary(coupon_code))