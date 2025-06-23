# def revSt(str):
#     return str[::-1]
# print(revSt('hello'))


# def sumOfEven(list):
#     sum = 0
#     for i in list:
#         if i % 2 == 0:
#             sum += i
#     else:
#         return sum
# print(sumOfEven([1, 2, 3, 4, 5, 6])) 


# def fbz(nums):
#     for num in nums:
#         if num % 5 == 0 and num % 3 == 0:
#             return 'FizzBuzz'
#         elif num % 5 == 0:
#             return  'Buzz'
#         elif num % 3 == 0:
#             return 'Fizz'
# def fbz():
#     for num in range(1, 21):
#         if num % 3 == 0 and num % 5 == 0:
#             print("FizzBuzz")
#         elif num % 5 == 0:
#             print("Buzz")
#         elif num % 3 == 0:
#             print("Fizz")
#         else:
#             print(num)

# fbz()


# def listFilter(listOfN):
#     result = []
#     for i in listOfN:
#         if i > 10:
#             result.append(i)
#     return result

# print(listFilter([3,12,8,25,7,30]))


# grades = {
#     "Andrea": 95,
#     "Chris": 82,
#     "Taylor": 91,
#     "Jordan": 76
# }


# def topg(grades):
#     result = []
#     for i in grades:
#         if grades[i] > 90:
#             result.append(i)
#     return result
# print(topg(grades))



# students = {
#     "Andrea": {"math": 95, "science": 88},
#     "Chris": {"math": 82, "science": 90},
#     "Taylor": {"math": 91, "science": 85}
# }


# def nd(students):
#     result = []
#     for student in students:
#         if students[student]['math'] > 90:
#             result.append(student)
#     return result

# print(nd(students))

# Write a function that returns the average salary of employees in the 'IT' department.
# employees = {
#     "Alice": {"age": 30, "department": "HR", "salary": 70000},
#     "Bob": {"age": 45, "department": "IT", "salary": 90000},
#     "Charlie": {"age": 25, "department": "IT", "salary": 85000},
#     "Diana": {"age": 40, "department": "Finance", "salary": 95000}
# }



# def avgSal(employees):
#     result = []
#     avg = 0
#     for e in employees:
#         if employees[e]['department'] == 'IT':
#             result.append(employees[e]['salary'])
#     total = sum(result)
#     count = len(result)
#     avg = total / count
#     return avg 

# print(avgSal(employees))
       

# Write a function that returns how many people like "apple" as their favorite fruit.
# favorites = {
#     "Andrea": {"fruit": "apple"},
#     "Chris": {"fruit": "banana"},
#     "Taylor": {"fruit": "apple"},
#     "Jordan": {"fruit": "grape"},
#     "Morgan": {"fruit": "apple"}
# }

# def apple(favorites):
#     count = 0
#     for fav in favorites:
#         if favorites[fav]['fruit'] == 'apple':
#             count += 1
#     return count
        
# print(apple(favorites))
    

pets = {
    "Louie": {"type": "cat", "age": 5},
    "Bella": {"type": "dog", "age": 3},
    "Max": {"type": "dog", "age": 7},
    "Milo": {"type": "cat", "age": 2},
    "Buddy": {"type": "dog", "age": 4}
}

def howManyDogs(pets):
    count = 0
    for item in pets:
        if pets[item]['type'] == 'dog':
            count += 1
    return count
print(howManyDogs(pets))


