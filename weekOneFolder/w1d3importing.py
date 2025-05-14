# 🧠 What Does “Importing” Mean?
# In Python, importing means bringing in code from another module, file, or library so you can use its functions, classes, or variables in your current file.

# 📦 Package
# A package is a way of organizing related Python modules together in a directory.
# It’s just a folder with a special file called __init__.py inside it (even if it's empty).
# Think of it like a toolbox filled with different tools (modules) grouped by purpose.
#  Example: numpy is a package that contains modules for mathematical functions.

# 📄 Module
# A module is a single Python file (.py) that contains functions, classes, or variables you can use in your own code.
# It helps you reuse and organize code.
# 🧠 Example: A file named math_tools.py with custom math functions is a module.

#  Standard Library
# This is a collection of modules and packages that come with Python.
# You don’t need to install them separately — just import and use.
# 🧠 Examples: math, random, datetime, os

# 🌍 Third-Party Library
# These are modules or packages created by other developers, not included with Python by default.
# You install them using tools like pip.
# 🧠 Examples: requests (for web requests), pandas (for data), flask (for web apps)

# 🧠 Namespace
# A namespace is like a labeled space in memory where names (like variables or functions) are stored.
# It helps avoid name conflicts between different parts of code.

import numpy as np

result = np.add(3,5)
print(f'the sum of 3 and 5 is {result}.')
result = np.multiply(4,6)
print(f'the product of 4*6 is {result}.')

import sys
print('Python looks for modules in these locations: ')
for path in sys.path:
    print(f'-{path}')

import mathfunction

result = mathfunction.add(3,5)
print(f'the sum of 3 and 5 is {result}.')
result2 = mathfunction.subtract(10,5)
print(f'diff of 10 and 5 is {result2}')

# import math
# print(f'the value of ppi is = {math.pi}')
# print(f'the value of e is approx {math.e}')
# print(f'square root of 16 = {math.sqrt(16)}')
# print(f'sin of 90 deg = {math.sin(math.radians(90))}')
# print(f'the factorial of 5 is {math.factorial(5)}')

# import datetime as dt
# now = dt.datetime.now()
# print({now})

# future_date = dt.datetime(2026,12,41)
# print({future_date})

# numpy is the most popular library for python, u have to install it


# import numpy as np
# array1 = np.array([1,2,3,4,5])





