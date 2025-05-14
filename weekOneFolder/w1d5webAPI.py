#  What is an API?
# API stands for Application Programming Interface.
# It allows different software systems to communicate with each other.
# Think of it like a menu in a restaurant – it tells you what you can ask for, and the kitchen (the server) delivers it.
# Web APIs – accessed using HTTP (e.g., REST APIs)
# Types of APIs
# Library APIs – functions provided by libraries in a programming language
# Operating System APIs – like Windows or macOS APIs for accessing system resources
#  REST API (Common Web API)
# REST = Representational State Transfer
# Uses standard HTTP methods:
# GET – retrieve data
# POST – create data
# PUT – update data
# DELETE – remove data

#  API Components
# Endpoint – the URL where the API can be accessed
# Example: https://api.example.com/users
# Request – what you send (method, headers, body)
# Response – what you get back (status, headers, body/data)
# Making an API Request (Python Example)

# import requests 

# # Define the URL
# url = 'https://jsonplaceholder.typicode.com/posts/1'

# # Make a GET request
# response = requests.get(url)

# # Check the response
# if response.status_code == 200:
#     data = response.json()  # Safely parse JSON
#     print(data)
# else:
#     print("Error:", response.status_code)



# import requests

# # Define the URL
# url = 'https://jsonplaceholder.typicode.com/posts/1'

# # Make a GET request
# response = requests.get(url)

# # Check the response
# if response.status_code == 200:
#     data = response.json()  # Safely parse JSON
#     print(data)
# else:
#     print("Error:", response.status_code)



#  Common Response Codes
# 200 OK – success
# 201 Created – new resource created
# 400 Bad Request – client error
# 401 Unauthorized – need login/token
# 404 Not Found – wrong endpoint
# 500 Server Error – something broke on their end
#  Auth in APIs
# API Key – a token you send in headers or URL
# OAuth – for more secure user login and access

# WENT TO OFFICE HOURS 4-19, TRIED TO FIGURE OUT WHAT THE DEAL WAS ABOUT TRYING TO IMPORT 
# REQUESTS FROM THIS FILE. HAD NO LUCK FIXING THE ISSUE.


