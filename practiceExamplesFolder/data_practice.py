# import pandas as pd
# from datetime import datetime

# # Create a date range for 10 days starting May 1, 2024
# dates = pd.date_range(start='2024-05-01', periods=10, freq='D')

# # Daily steps data
# steps = [5000, 7000, 6500, 8000, 9000, 7500, 8500, 10000, 11000, 9500]

# # Create DataFrame with DateTimeIndex
# df = pd.DataFrame({'steps': steps}, index=dates)

# print(df)
# # Get steps for May 3rd to May 6th
# print(df['2024-05-03':'2024-05-06'])

# weekly_steps = df.resample('W').sum()
# print(weekly_steps)
# # Shift all dates by 2 business days (e.g. skipping weekends)
# df_shifted = df.shift(freq='2B')
# print(df_shifted)

# ts = pd.Timestamp('2024-05-05')
# print("Day of week for", ts, "is", ts.day_name())


# bookstore = {
#     "fiction": {
#         "1984": {"price": 9.99, "stock": 12},
#         "brave_new_world": {"price": 8.99, "stock": 5}
#     },
#     "nonfiction": {
#         "sapiens": {"price": 14.99, "stock": 7},
#         "educated": {"price": 13.99, "stock": 4}
#     },
#     "comics": {
#         "spiderman": {"price": 5.99, "stock": 10},
#         "batman": {"price": 6.99, "stock": 8}
#     }
# }

# def add_book(inventory, category, title, price, stock):
#     """Add a new book to a category."""
#     if category not in inventory:
#         inventory[category] = {}
    
#     inventory[category][title] = {'price': price,'stock': stock }

# add_book(bookstore, 'fiction', 'the firm', 19.99,5)
# print(bookstore)



# def remove_book(inventory, category, title):
#     """Remove a book from a category."""
#     if category in inventory:
#         if title in inventory[category]:
#             del inventory[category][title]

# remove_book(bookstore, 'fiction', 'the firm')
# print('after del==',bookstore)


# def list_all_titles(inventory, category):
#     """Return a list of all book titles in the specified category."""
#     if category in inventory:
#         return list(inventory[category].keys())
#     else:
#         return []
# print(list_all_titles(bookstore, category="fiction"))


# def expensive_books(inventory, min_price):
#     """Return a list of all book titles with price above min_price across all categories."""
#     result = []
#     for category in inventory.values():
#         for title, info in category.items():
#             if info['price'] > min_price:
#                 result.append(title)
#     return result
# print(expensive_books(bookstore, 10))

# def books_below_stock(inventory, max_stock):
#     """Return a list of book titles with stock less than max_stock."""
#     result = []
#     # Step 1: Loop through categories in the inventory
#     for categories in inventory.values():
#         for title, info in categories.items():
#             if info['stock'] < max_stock:
#                 result.append(title)
#     # Step 2: Loop through books in each category
    
#     # Step 3: Check if stock is less than max_stock
    
#     # Step 4: If yes, add the title to result list
    
#     # Step 5: Return the result list
#     return result
# print(books_below_stock(bookstore, 12))


# def count_even_numbers(numbers):
#     count = 0
#     for item in numbers:
#         if item % 2 == 0:
#             count += 1
#     return count
# print(count_even_numbers([1,2,3,4,5,6]))

# def filter_long_words(words, min_length):
#     result = []
#     for word in words:
#         if len(word)>= min_length:
#             result.append(word)
#     return result
# print(filter_long_words(['a','bc', 'def','ghijk'],3))

# def reverse_list(items):
#     revL = []
#     n = len(items)
#     for item in range(n-1,-1,-1):
#         revL.append(items[item])
#     return revL

# print(reverse_list([1,2,3,4]))

# movie_store = {
#     "action": {
#         "die_hard": {"price": 3.99, "stock": 5},
#         "mad_max": {"price": 4.99, "stock": 3}
#     },
#     "comedy": {
#         "superbad": {"price": 2.99, "stock": 7},
#         "step_brothers": {"price": 3.49, "stock": 4}
#     },
#     "drama": {
#         "the_godfather": {"price": 5.99, "stock": 2},
#         "shawshank_redemption": {"price": 4.49, "stock": 6}
#     }
# }
# # Tasks:
# # Add a movie
# # Write add_movie(store, category, title, price, stock) — adds a new movie to the store.
# def add_movie(store, category, title, price, stock):
#     if category not in store:
#         store[category] = {}
#     store[category][title] = {'price': price, 'stock': stock}
# add_movie(movie_store, 'action', 'terminator', 4.50, 6)
# print(movie_store['action'])


# # Remove a movie
# # Write remove_movie(store, category, title) — removes the movie from the store.
# def remove_movie(store, category, title):
#     if category in store:
#         if title in store[category]:
#             del store[category][title]

# remove_movie(movie_store, 'action', 'terminator')
# print(movie_store)

# def filter_words(words, min_len):
#     result = []
#     for word in words:
#         if len(word) >= min_len:
#             result.append(word)
#     return result
# print(filter_words(['cat', 'dog', 'elephant', 'bee'], 4))  # should return ['elephant']

# def words_starting_w(words, letter):
#     result = []
#     for word in words:
#         if word[0].lower() == letter.lower():
#             result.append(word)
#     return result
# print(words_starting_w(['apple', 'banana', 'Avocado', 'grape'], 'a'))
# # should return ['apple', 'Avocado']


# def words_ending_w(words, letter):
#     result = []
#     for word in words:
#         if word[-1].lower() == letter.lower():
#             result.append(word)
#     return result
# print(words_ending_w(['cat', 'dog', 'apple', 'banana', 'grape'], 'e')
# # should return ['apple', 'grape']
# )

# def count_words_longer_than(words, length):

#     count = 0
#     for word in words:
#         if len(word) > length:
#             count +=1
#     return count

        
# print(count_words_longer_than(['cat', 'elephant', 'dog', 'bee'], 3) ) # should return 1

# def sum_nums_greater_than(listofnums, thresholdnum):
#     sum = 0
#     for number in listofnums:
#         if number > thresholdnum:
#             sum += number
#     return sum
# print(sum_nums_greater_than([1, 5, 10, 20, 3], 6) ) # should return 30 (10 + 20)

# def count_words(words):
#     result = {}
#     for word in words:
#         if word in result:
#             result[word] += 1
#         else:
#             result[word] = 1
#     return result
# print(count_words(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))
# # Output: {'apple': 3, 'banana': 2, 'orange': 1}     
# 
# 
# def count_even_odd(nums):
#     result = {'evens': 0, 'odds': 0}
#     for num in nums:
#         if num % 2 == 0:
#             result['evens'] +=1
#         else:
#             result['odds'] += 1
#     return result
# print(count_even_odd([1, 2, 3, 4, 5, 6]))


# def count_odds(nums):
#     result = {'odds': 0, 'evens': 0}
#     for num in nums:
#         if num % 2 != 0:
#             result['odds'] += 1
#         else:
#             result['evens'] +=1
#     return result
# print(count_odds([1, 2, 3, 4, 5, 6,7,7,7,]))

def group_by_length(words):
    result ={}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
       
            result[length].append(word)
            print(f"After adding '{word}': {result}")  # <-- debug pri
    return result
print(group_by_length(['cat', 'dog', 'elephant', 'bee', 'ant']))


