# # Nested data in Python refers to data structures that contain other data structures, allowing for more complex and multi-level data representation. Here are some key notes on nested data in Python:

# # 1. Lists of Lists
# # A list can contain other lists as its elements. This is a common way to organize data in multiple dimensions, like matrices.

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # To access an element: nested_list[0][1] will return 2 (first list, second element).

# # 2. Dictionaries Containing Lists (and vice versa)
# # Dictionaries can contain lists as values, and lists can contain dictionaries as elements. This allows for structured and complex data representations.

# nested_dict = {
#     "name": "John",
#     "contact": ["email@example.com", "555-1234"],
#     "address": {"street": "123 Main St", "city": "Somewhere"}
# }
# # To access a value from the dictionary: nested_dict["contact"][0] will return "email@example.com".

# # To access a value from the nested dictionary: nested_dict["address"]["city"] will return "Somewhere".

# # 3. Dictionaries of Dictionaries
# # You can also nest dictionaries inside each other. This is useful for organizing hierarchical data.


# students = {
#     "John": {"age": 20, "grades": [85, 90, 92]},
#     "Alice": {"age": 22, "grades": [88, 91, 94]}
# }
# # To access John’s age: students["John"]["age"] will return 20.

# # To access Alice’s grades: students["Alice"]["grades"] will return [88, 91, 94].

# # 4. Accessing Nested Data
# # To access nested data, you can use multiple indexing or key references. The structure you follow depends on the data type (list or dictionary).


# nested_data = [
#     {"name": "Item1", "value": 10},
#     {"name": "Item2", "value": 20}
# ]

# # Accessing Item2's value
# value = nested_data[1]["value"]  # 20

# # 5. Loops and Nested Loops
# # When working with nested data, it’s common to use loops to iterate through the data.

# # Example (nested lists):

# nested_list = [[1, 2], [3, 4], [5, 6]]
# for sublist in nested_list:
#     for item in sublist:
#         print(item)
# # This will print each number from the nested lists:
# 1
# 2
# 3
# 4
# 5
# 6

# nested_dict = {
#     "John": {"age": 20, "grades": [85, 90, 92]},
#     "Alice": {"age": 22, "grades": [88, 91, 94]}
# }


# for name, details in nested_dict.items():
#     print(f"{name}: {details['age']}")
# # This will print:

# John: 20
# Alice: 22

# 6. Modifying Nested Data
# You can modify nested data just like any other variable in Python by assigning new values.


# nested_list[0][1] = 100  # Changing the second element of the first sublist
# # Example (modifying a nested dictionary):

# nested_dict["John"]["age"] = 21  # Updating John's age to 21

# # 7. Handling Errors in Nested Data
# # When working with nested data, ensure you handle cases where an index or key might not exist, using try-except or checking if the key exists with if statements.


# nested_dict = {
#     "name": "John",
#     "contact": {"email": "john@example.com"}
# }

# # Safely accessing a non-existent key
# email = nested_dict.get("contact", {}).get("email", "No email found")
# print(email)  # Will print "john@example.com"

# # Nested Data In-Class Examples

# cart = {
#     'fruits': ['mango', 'apples', 'oranges'],
#     'veggies': ['spinach', 'peas'],
#     'grains': ['rice'],
#     'other': ['olive oil', 'pepper'],
#     'total': 24.75
# }
# print(cart)
# veg = cart['veggies']
# print('veg in cart', type(veg))
# print(veg)
# firstFruit = cart['fruits'][0]
# print(firstFruit)
# cart['veggies'].append('bell peppers')
# print("updated veggies:", cart["veggies"])
# cart['fruits'][0] = 'papaya'
# print(cart["fruits"])
# cart['dairy'] = ['milk', 'cheese']
# print('uppdated cart', cart)
# print(cart['fruits'])
# for fruit in cart['fruits']:
#     print(f'-{fruit}')

# print('all items by category:')
# for category, items in cart.items():
#     if isinstance(items, list):
#         print(f'{category.title()}')
#         for item in items:
#             print(f'-{item}')
#     else:
#         print(f'{category.title()}: {items}')

        # Real-World Example - Recipe Ingredients:
# A recipe with ingredients organized by category
# recipe = {
#     'name': 'Vegetable Stir Fry',
#     'prep_time': 15,
#     'cook_time': 10,
#     'servings': 4,
#     'ingredients': {
#         'proteins': ['tofu', 'cashews'],
#         'vegetables': ['bell pepper', 'broccoli', 'carrot', 'snow peas'],
#         'aromatics': ['garlic', 'ginger', 'green onion'],
#         'sauce': ['soy sauce', 'sesame oil', 'corn starch']
#     },
#     'steps': [
#         'Press and cube tofu',
#         'Chop all vegetables',
#         'Mix sauce ingredients',
#         'Stir-fry aromatics',
#         'Add vegetables and tofu',
#         'Add sauce and simmer'
#     ]
# }
# print(f'ing for {recipe["name"]} (Serves {recipe["servings"]})')
# for category, items in recipe['ingredients'].items():
#     print(f'{category.title()}')
#     for item in items:
#         print(f'-{item}')

# Start with this basic structure
# music_library = {
#     "rock": [
#         {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 354},
#         {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "duration": 482}
#     ],
#     "pop": [
#         {"title": "Shape of You", "artist": "Ed Sheeran", "duration": 234},
#         {"title": "Blinding Lights", "artist": "The Weeknd", "duration": 201}
#     ],
#     "hip-hop": [
#         {"title": "Lose Yourself", "artist": "Eminem", "duration": 326}
#     ]
# }

# # Task 1: Add a new song to the "rock" genre
# # Your code here
# new_rock_song = {
#     'title': 'SLTS',
#     'artist' : 'Nirvana',
#     'duration': 333
# }
# new_rock_song = music_library["rock"].append(new_rock_song)
# print(music_library)
# # Task 2: Print all songs in the "pop" genre
# # Your code here


# for song in music_library['pop']:
#     print(f'- {song['title']} by {song['artist']} ({song['duration']})')


# # Task 3: Calculate the total duration of all songs in "hip-hop"
# # Your code here
# total = 0
# for song in music_library['hip-hop']:
#     total += song['duration']
# print(total)

# Nested Dictionaries

# restaurants = {
#     'Amendolas': {
#         'address': '28 Lake St, Monroe, NY 10950',
#           'menu_url': 'https://www.amendolaspizzapasta.com/'
#     },
#     'LaVera Cucina': {
#         'address': '43 Hillside Terrace, Monroe, NY 10950',
#         'menu_url': 'https://www.veramonroe.com/'
#     }
# }
# print("Restaurant information:")
# print(restaurants)
# # Accessing Data in Nested Dictionaries:
# # Access information about a specific restaurant
# sri_info = restaurants['LaVera Cucina']
# print("LaVera Cucina info:", sri_info)
# # Access a specific piece of information
# el_basurero_address = restaurants['Amendolas']['address']
# print("Amendolas address:", el_basurero_address)
# # Using get() with a default value for safer access
# el_basurero_phone = restaurants.get('Amendolas', {}).get('phone', 'Not available')
# print("Amendolas phone:", el_basurero_phone)
# # Modifying Nested Dictionaries:
# # Add a new restaurant
# restaurants['Joes Pizza'] = {
#     'address': '7 Carmine St, New York, NY 10014',
#     'phone': '212-366-1182'
# }
# print("Added Joe's Pizza:", restaurants['Joes Pizza'])
# # Add a new field to an existing restaurant
# restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com'
# print("Updated Joe's Pizza:", restaurants['Joes Pizza'])
# # Update an existing field
# restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com/menu.php'
# # Remove a field
# restaurants['Joes Pizza'].pop('phone')
# print("Joe's Pizza after removing phone:", restaurants['Joes Pizza'])
# # Iterating Through Nested Dictionaries:
# # Print all restaurant information in a formatted way
# print("\nAll Restaurants:")
# for restaurant_name, details in restaurants.items():
#     print(f"\n{restaurant_name}:")
#     for key, value in details.items():
#         print(f"  {key}: {value}")


# Real-World Example - Product Inventory:
# A product inventory system
# inventory = {
#     'electronics': {
#         'smartphones': {
#             'iPhone 13': {'price': 799, 'stock': 15, 'colors': ['black', 'white', 'red']},
#             'Samsung Galaxy S21': {'price': 699, 'stock': 10, 'colors': ['black', 'silver']}
#         },
#         'laptops': {
#             'MacBook Pro': {'price': 1299, 'stock': 5, 'specs': {'ram': '16GB', 'storage': '512GB'}},
#             'Dell XPS': {'price': 999, 'stock': 8, 'specs': {'ram': '8GB', 'storage': '256GB'}}
#         }
#     },
#     'clothing': {
#         't-shirts': {
#             'Basic Tee': {'price': 19.99, 'stock': 50, 'sizes': ['S', 'M', 'L', 'XL']},
#             'Graphic Tee': {'price': 24.99, 'stock': 35, 'sizes': ['M', 'L']}
#         }
#     }
# }

# # Print all products with low stock (less than 10)
# print("\nLow Stock Items:")
# for category, subcategories in inventory.items():
#     for subcategory, products in subcategories.items():
#         for product, details in products.items():
#             if details['stock'] < 10:
#                 print(f"{category} - {subcategory} - {product}: Only {details['stock']} left!")

# Start with this basic structure


# school = {
#     "Computer Science": {
#         "chair": "Dr. Jane Smith",
#         "courses": {
#             "CS101": {"name": "Intro to Programming", "instructor": "Dr. Brown", "credits": 3},
#             "CS201": {"name": "Data Structures", "instructor": "Dr. Green", "credits": 4}
#         }
#     },
#     "Mathematics": {
#         "chair": "Dr. Tom Johnson",
#         "courses": {
#             "MATH101": {"name": "Calculus I", "instructor": "Dr. White", "credits": 4},
#             "MATH205": {"name": "Linear Algebra", "instructor": "Dr. Brown", "credits": 3}
#         }
#     }
# }

# # Task 1: Add a new course "CS301: Database Systems" to Computer Science
# # taught by "Dr. Lee" with 4 credits
# # Your code here

# school['Computer Science']['courses']['CS301'] = {
#     'name': 'Database Systems',
#     'instructor': 'Dr. Lee',
#     'credits': 4
# }

# # Task 2: Find and print all courses taught by "Dr. Brown"
# # Your code here
# print('Courses taught by Dr. Brown:')
# for department, info in school.items():
#     for course, details in info['courses'].items():
#         if details['instructor'] == 'Dr. Brown':
#             print(f'{course} {details['name']} {department}')
        

# # Task 3: Print a formatted list of all departments and their courses
# # Your code here

# print('Formatted list of depts and courses: ')
# for dept, info in school.items():
#     print('Dept=', {department})
#     print(f'Chair:', {info['chair']})
#     for course, details in info['courses'].items():
#          print(f"  {course}: {details['name']} | Instructor: {details['instructor']} | Credits: {details['credits']}")


    
    
# # Live Coding Example - Basic List of Dictionaries:
# # A list of user dictionaries
# users = [
#     {'username': 'ash', 'password': 'ilovepython', 'last_login': '9/28/2020'},
#     {'username': 'aryn', 'password': 'ilovedictionaries'},
#     {'username': 'yusuf', 'password': 'ilovejavascript', 'last_login': '9/26/2020'},
#     {'username': 'paul', 'password': 'ilovegit'}
# ]

# print("User accounts:")
# print(users)

# # Accessing Data in Lists of Dictionaries:
# # Access a specific dictionary from the list
# yusuf_account = users[2]
# print("\nYusuf's account:", yusuf_account)

# # Modifying Lists of Dictionaries:
# # Add a new user to the list
# users.append({'username': 'aeshna', 'password': 'ilovesublimetxt'})
# print("\nAdded a new user:", users[-1])

# # Modify an existing user's data
# users[2]['verified_account'] = True
# users[2]['password'] = 'iloveprogramming'
# users[2].pop('last_login', None)
# print("Modified Yusuf's account:", users[2])

# # Iterating Through Lists of Dictionaries:
# # Print all usernames
# print("\nAll usernames:")
# for user in users:
#     print(user['username'])

# # Convert all usernames to uppercase
# for user in users:
#     user['username'] = user['username'].upper()

# print("\nUsernames after uppercase conversion:")
# for user in users:
#     print(user['username'])

# # Print all users with a 'last_login' field
# print("\nUsers with last login information:")
# for user in users:
#     if 'last_login' in user:
#         print(f"{user['username']} last logged in on {user['last_login']}")

# # Real-World Example - Task Management:
# # A task management system
# tasks = [
#     {'id': 1, 'title': 'Finish project proposal', 'status': 'completed', 'assigned_to': 'Alice', 'due_date': '2025-04-01'},
#     {'id': 2, 'title': 'Review code', 'status': 'in progress', 'assigned_to': 'Bob', 'due_date': '2025-04-10'},
#     {'id': 3, 'title': 'Fix bugs', 'status': 'in progress', 'assigned_to': 'Alice', 'due_date': '2025-04-15'},
#     {'id': 4, 'title': 'Deploy application', 'status': 'pending', 'assigned_to': 'Charlie', 'due_date': '2025-04-20'},
#     {'id': 5, 'title': 'Write documentation', 'status': 'pending', 'assigned_to': 'Bob', 'due_date': '2025-04-25'}
# ]

# # Find all tasks assigned to Alice
# alice_tasks = [task for task in tasks if task['assigned_to'] == 'Alice']
# print("\nAlice's tasks:")
# for task in alice_tasks:
#     print(f"- {task['title']} ({task['status']})")

# # Count tasks by status
# status_count = {}
# for task in tasks:
#     status = task['status']
#     if status in status_count:
#         status_count[status] += 1
#     else:
#         status_count[status] = 1

# print("\nTask status summary:")
# for status, count in status_count.items():
#     print(f"{status}: {count} tasks")

# # Find overdue tasks (assuming today is April 15, 2025)
# today = '2025-04-15'
# overdue_tasks = [task for task in tasks if task['status'] != 'completed' and task['due_date'] < today]
# print("\nOverdue tasks:")
# for task in overdue_tasks:
#     print(f"- {task['title']} (Due: {task['due_date']}, Assigned to: {task['assigned_to']})")

# today = '2025-04-15'
# pending_tasks = []
# for task in pending_tasks:
#     if task['status'] != 'completed' and task['duedate'] < today:
#         pending_tasks.append(task)
# print('\nOverdue tasks:')
# for task in pending_tasks:
#     print(f'- {task['title']} (Due: {task['due_date']}, Assigned to: {task['assigned_to']})')


# shopping_list = [
#     ['mangos', 'apples', 'oranges', 'grapes'],
#     ['carrots', 'broccoli', 'lettuce'],
#     ['corn flakes', 'oatmeal']
# ]

# print("Shopping list by category:")
# print(shopping_list)

# # # Accessing Data in Nested Lists:
# # # Access a specific item
# item = shopping_list[0][1]
# print("\nThe second item in the first category is:", item)  # apples

# # # Access the last category
# last_category = shopping_list[-1]
# print("Last category:", last_category)  # ['corn flakes', 'oatmeal']

# # # Modifying Nested Lists:
# # # Add an item to the first category
# shopping_list[0].append('bananas')
# print("\nAdded bananas to first category:", shopping_list[0])

# # # Replace an item in the second category
# shopping_list[1][0] = 'baby carrots'
# print("Updated second category:", shopping_list[1])

# # # Add a whole new category
# shopping_list.append(['milk', 'cheese', 'yogurt'])
# print("Added a new category:", shopping_list[-1])

# # # Iterating Through Nested Lists:
# # # Loop through all items in the shopping list
# print("\nAll shopping list items:")
# for category in shopping_list:
#     for item in category:
#         print(f"- {item}")

# # # Loop with a counter
# print("\nNumbered shopping list:")
# counter = 1
# for category in shopping_list:
#     for item in category:
#         print(f"{counter}. {item}")
#         counter += 1

# # # Filter items containing 'a'
# print("\nItems containing 'a':")
# for category in shopping_list:
#     for item in category:
#         if 'a' in item:
#             print(f"- {item}")



import json

student_data = {
    'name': 'Alice Johnson',
    'age': 22,
    'courses': ['Python Programming', 'Data Structures', 'Algorithms'],
    'grades': {
        'Python Programming': 95,
        'Data Structures': 88,
        'Algorithms': 91
    },
    'contact': {
        'email': 'alice@example.com',
        'phone': '555-123-4567',
        'address': {
            'street': '123 Campus Dr',
            'city': 'University Town',
            'state': 'CA',
            'zip': '94305'
        }
    }
}

# Convert to JSON string



json_data = json.dumps(student_data, indent=4)
print("\nJSON representation of student data:")
print(json_data)

# Convert JSON string back to Python
python_data = json.loads(json_data)
print("\nConverted back to Python:")
print(type(python_data))

# Read/write JSON to a file
with open('student.json', 'w') as f:
    json.dump(student_data, f, indent=4)

print("\nWritten to student.json")

with open('student.json', 'r') as f:
    loaded_data = json.load(f)

print("Successfully loaded from file")

# Real-World Example - API Data:
# Sample API response for a weather service
weather_api_response = {
    "location": {
        "name": "New York",
        "region": "New York",
        "country": "United States",
        "lat": 40.71,
        "lon": -74.01,
        "timezone": "America/New_York"
    },
    "current": {
        "temp_f": 72.5,
        "condition": {
            "text": "Partly cloudy",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png"
        },
        "humidity": 65,
        "wind_mph": 10.5,
        "precip_in": 0.0
    },
    "forecast": {
        "forecastday": [
            {
                "date": "2025-04-08",
                "day": {
                    "maxtemp_f": 75.6,
                    "mintemp_f": 62.1,
                    "condition": {
                        "text": "Sunny",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png"
                    }
                },
                "hour": [
                    {"time": "2025-04-08 00:00", "temp_f": 65.3},
                    {"time": "2025-04-08 01:00", "temp_f": 64.8},
                    {"time": "2025-04-08 02:00", "temp_f": 64.0}
                ]
            },
            {
                "date": "2025-04-09",
                "day": {
                    "maxtemp_f": 78.2,
                    "mintemp_f": 63.5,
                    "condition": {
                        "text": "Cloudy",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/119.png"
                    }
                },
                "hour": [
                    {"time": "2025-04-09 00:00", "temp_f": 66.2},
                    {"time": "2025-04-09 01:00", "temp_f": 65.7},
                    {"time": "2025-04-09 02:00", "temp_f": 65.1}
                ]
            }
        ]
    }
}

# Extract and display weather information
location_name = weather_api_response["location"]["name"]
current_temp = weather_api_response["current"]["temp_f"]
current_condition = weather_api_response["current"]["condition"]["text"]

print(f"\nCurrent weather in {location_name}: {current_temp}°F, {current_condition}")

# Process forecast data
print("\nForecast:")
for day in weather_api_response["forecast"]["forecastday"]:
    date = day["date"]
    max_temp = day["day"]["maxtemp_f"]
    min_temp = day["day"]["mintemp_f"]
    condition = day["day"]["condition"]["text"]
    
    print(f"{date}: {min_temp}°F to {max_temp}°F, {condition}")