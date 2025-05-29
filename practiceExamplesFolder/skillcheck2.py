# 🔁 List & Dictionary Practice Challenge (No Functions Yet)
# Pretend you’re tracking your favorite songs with ratings.

# Step 1: Create a list of dictionaries
# Create a list called my_songs that looks like this:

my_songs = [
    {"title": "Golden Hour", "artist": "JVKE", "rating": 4.8},
    {"title": "Vampire", "artist": "Olivia Rodrigo", "rating": 4.6},
    {"title": "Peaches", "artist": "Justin Bieber", "rating": 3.9}
]
# Step 2: Print each song's title and rating
# Use a for loop to print something like:

# for song in my_songs:
#     print(f'{song['title']} has a rating of {song['rating']}')
# # Golden Hour has a rating of 4.8
# # Vampire has a rating of 4.6
# # Peaches has a rating of 3.9
# # Step 3: Add a new song to the list
# # Append a new dictionary to my_songs.
# # Step 3: Add a new song to the list
# my_songs.append({"title": "Hello World", "artist": "Me", "rating": 5.0})

# # Print to check
# for song in my_songs:
#     # print(f"{song['title']} has a rating of {song['rating']}")

# # Step 4: Update the rating of one song
# # Change the rating of “Peaches” to 4.2.
# # Step 4: Update the rating of “Peaches” to 4.2
# for song in my_songs:
#     if song['title'] == 'Peaches':
#         song['rating'] = 4.2

# # Print to check the update
# for song in my_songs:
    # print(f"{song['title']} has a rating of {song['rating']}")

# Step 5: Print the average rating of all songs
# Loop through and calculate the average.
# total_rating = 0
# for song in my_songs:
#     total_rating += song['rating']

# average_rating = total_rating / len(my_songs)
# print(f"The average rating is {average_rating:.2f}")

# If you want an extra challenge:

# Print only the songs with a rating higher than 4.5.

# Sort the list by rating (manually, not with sort() just yet—unless you want to experiment).
# print("Songs with rating > 4.5:")
# for song in my_songs:
#     if song['rating'] > 4.5:
#         print(f"{song['title']} - Rating: {song['rating']}")

# for i in range(1, len(my_songs)):
#     print(f"Current index: {i}, Current song: {my_songs[i]}")
#     print(f"Previous song: {my_songs[i-1]}")

# my_movies = [
#     {"title": "Inception", "rating": 4.7},
#     {"title": "The Matrix", "rating": 4.5},
#     {"title": "Interstellar", "rating": 4.6},
#     {"title": "The Room", "rating": 2.5}
# ]

# # Step 1: Print each movie and rating
# for movie in my_movies:
#     print(f"{movie['title']} has a rating of {movie['rating']}")

# # Step 2: Write a function to calculate average rating
# def average_rating(movies):
#     total = 0
#     for movie in movies:  # loop over the movies list
#         total += movie['rating']  # add each movie's rating to total
#     avg = total / len(movies)
#     return avg

# avg = average_rating(my_movies)
# print(f"The average rating is {avg}")

    



# # Step 3: Print movies with rating above average
# # Your code here
# for movie in my_movies:
#     if movie['rating']>avg:
#         print(f'{movie['title']}{movie["rating"]}')

# myFav = ["books", "sunshine", "coffee", "yoga", "candles"]
# def myFavs(lst):
#     result = []
#     for item in lst:
#         if len(item) > 5:
#             result.append(item)
#     return result
# print(myFavs( ["books", "sunshine", "coffee", "yoga", "candles"]))


# def shortW(lst):
#     result = []
#     for i in lst:
#         if len(i) <= 4:
#             result.append(i)
#     return len(result)
# print(shortW(["tree", "sun", "cloud", "air", "sky"]))

# def countevens(nums):
#     count = 0
#     for i in nums:
#         if i % 2 == 0:
#             count +=1
#     return count
# print(countevens([3,4,7,10,12,15]))

# def startWs(lst):
#     result = []
#     for item in lst:
#         if item[0] == 's' or item[0] == 'S':
#             result.append(item)
#     return result
# print(startWs(["Sun", "moon", "stars", "Sky", "galaxy"]))


# student = {
#     "name": "Andrea",
#     "scores": {
#         "math": 85,
#         "english": 92,
#         "science": 78
#     }
# }

# mathScore = student["scores"]['math']
# engScore = student["scores"]['english']

# print(mathScore,engScore)

# student["scores"]['science'] = 82
# student['scores']['history'] = 90
# print(student)

# def seeScores(student):
#     result = {}
#     for key,value in student['scores'].items():
#         print('items=', key, value)
# seeScores(student)
# data = [
#     {"date": "2025-05-01", "temperature": 20, "humidity": 55},
#     {"date": "2025-05-02", "temperature": 22, "humidity": 65},
#     {"date": "2025-05-03", "temperature": 19, "humidity": 50}
# ]

# def filter_by_humidity(data, min_humidity):
#     result = []
#     for reading in data:
#         if reading['humidity'] >= min_humidity:
#             result.append(reading)
#     return result


# people = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Charlie", "age": 35},
#     {"name": "Diana", "age": 20}
# ]

# def filter_adults(people, min_age):
#     result = []
#     for item in people:
#         if item['age'] >= min_age:
#             result.append(item)
#     return result
# print(filter_adults(people,21))

# products = [
#     {"name": "laptop", "price": 999.99},
#     {"name": "phone", "price": 499.99},
#     {"name": "tablet", "price": 299.99},
#     {"name": "monitor", "price": 199.99}
# ]

# def get_expensive_products(products, threshold):
#     result = []
#     for item in products:
#         if item['price'] > threshold:
#             result.append(item['name'])
#     return result
# print(get_expensive_products(products,450))





# Practice Problem:
# Calculate total inventory value per category
# inventory = {
#     "produce": {
#         "apple": {"price": 0.5, "stock": 100},
#         "carrot": {"price": 0.2, "stock": 200},
#         "spinach": {"price": 1.0, "stock": 50}
#     },
#     "cereal": {
#         "cornflakes": {"price": 3.5, "stock": 25},
#         "froot_loops": {"price": 4.2, "stock": 15}
#     },
#     "snacks": {
#         "chips": {"price": 2.0, "stock": 40},
#         "granola_bar": {"price": 1.2, "stock": 30}
#     }
# }
# # Write a function called category_values(inventory) that:
# def category_values(inventory):
#     result = {}
#     for key,value in inventory.items():
# Takes this inventory dictionary as input

# Calculates the total value of stock in each category (price * stock for each item, then sum for the category)

# Returns a dictionary where keys are category names, and values are the total stock value (float) for that category.











