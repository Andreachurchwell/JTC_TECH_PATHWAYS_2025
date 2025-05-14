# import numpy as np
# msg = "Roll a dice!"
# print(msg)
# print(np.random.randint(1,9))

# print('hello world')

# x = 1
# print(x)
# x = x + 1
# print(x)
# exit()



# x = 5
# if x < 10:
#     print('smaller')
# if x > 20:
#     print('bigger')
# print('Finis')





# n = 5
# while n > 0 :
#     print(n)
#     n = n -1
# print('blastooff')




# x = 5
# print('hello')
# def print_lyrics():
#     print('ima lumberjack, and im okay')
# print('yo')
# print_lyrics()




# big = max('hello world')
# print(big)


# def addtow(a,b):
#     added = a + b
#     return added
# x = addtow(5,6)
# print(x)




# def thing():
#     print('Hello')

# print('There')  




# def func(x) :
#     print(x)

# func(10)
# func(20)



# def stuff():
#     print('Hello')
#     return
#     print('World')

# stuff()


# def addtwo(a, b):
#     added = a + b
#     return a

# x = addtwo(2, 7)
# print(x)

# while True:
#     line = input('> ')
#     if line == 'done' :
#         break
#     print(line)
# print('done')



# for i in [5,4,3,2,1] :
#     print(i)
# print("BLASTOFF")



# friends = ['andrea', 'pam', 'louie']
# for friend in friends :
#     print("HAPPY HAPPY:", friend)
# print("DONE")



# larg_sos_far = -1
# print('befire', larg_sos_far)
# for thenum in [3333,6,8,9,1,99, 102] :
#     if thenum > larg_sos_far :
#         larg_sos_far = thenum
#     print(larg_sos_far, thenum)
# print('after', larg_sos_far)





# zork = 0
# print('before', zork)
# for thing in [3,6,2,8,9,66] :
#     zork = zork + 1
#     print(zork, thing)
# print('after', zork)

# sum in loop
# zork = 0
# print('before', zork)



# for thing in [3,6,2,8,9,66] :
#     zork = zork + thing
#     print(zork, thing)
# print('after', zork)


# avg in loop
# count = 0
# sum = 0
# print('before', count, sum)
# for value in [1,2,3,4,5] :
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# print('after', count, sum, sum / count)



# filtering loop

# this is not working right!!!
# print('before')
# for value in [2,5,7,9,15] :
#     if value < 20:
#         print ('large number', value)
# print('after')




# using booleans
# found = False
# print('before', found)
# for value in [1,2,3,4,5] :
#     if value == 3 :
#         found = True
#     print(found, value)
# print('after==', found)



# smallest = None
# print('before')
# for thenum in [6,34,32,11,5,7] :
#     if smallest is None :
#         smallest = thenum
#     elif thenum < smallest :
#         smallest = thenum
#     print(smallest, thenum)
# print('after===', smallest)



# tot = 0 
# for i in [5, 4, 3, 2, 1] :
#     tot = tot + 1
# print(tot)



# zork = 0
# for thing in [9, 41, 12, 3, 74, 15] :
#     zork = zork + thing
# print('After', zork)



# smallest_so_far = -1
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num < smallest_so_far :
#       smallest_so_far = the_num
# print(smallest_so_far)



# num = 0
# tots = 0.0
# while True :
#     sval = input('ENTER A NUMBER: ')
#     if sval == 'done' :
#         break
#     try:
#         fval = float(sval)
#     except:
#         print('Invalid input')
#         continue
#     # print(fval)
#     num = num + 1
#     tots = tots + fval
# # print('all done')
# print(tots, num, tots/num)


# str1 = "Hello"
# str2 = 'there'
# bob = str1 + str2
# print(bob)
# x = '40'
# y = int(x) + 2
# print(y)
# print(len('banana')*7)
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(len(c))
# friends = [ 'Joseph', 'Glenn', 'Sally' ]
# friends.sort()
# print(friends[0])


# # definite Loops and dictionaries
# counts = { 'chuck' : 1 , 'andrea' : 42 , 'jan' : 100}
# for key in counts:
#     print(key, counts[key])

# retrieving list of keys and values
# jjj = { 'chuck' : 1 , 'andrea' : 42 , 'jan' : 100}
# print(list(jjj))
# print(list(jjj.keys()))
# print(list(jjj.values()))
# print(list(jjj.items()))

# two iteration variables
# better name for those will be key and values
# for aaa,bbb in jjj.items() :
#     print(aaa,bbb)

# chapter 9 coursera below:
# fname = input('enter file: ')
# if len(fname) < 1 : fname = 'clown.txt'

# fhand = open(fname)
# many = dict()


# for line in fhand :
#     line = line.rstrip()
#     # print(line)

#     wds = line.split()
#     # print(wds)

#     for w in wds:
#         print('++++>', w)
#         print('before********',many)
#         # oldVal = 0
#         # if w in many : oldVal = many[w]

#         oldVal = many.get(w,0)
#         many[w] = oldVal + 1
#         print('after************', many)

#         largest = None
#         bigword = None
#         for cle, valeur in many.items() :
#             print(cle, valeur)
#             if largest is None or largest > valeur :
#                 largest = valeur
#                 bigword = cle
# print('yay', bigword,largest)


# # tuples
# x = ('glen', 'ally', 'joe')
# print(x[2])
# # prints joe

# (x, y) = (4, 'fred')
# print(y)
# # prints fred


# c = {'a':10, 'b,':1.,'c':22}
# tmp = list()
# for k, v in c.items() :
#     tmp.append( (v,k) )

#     print(tmp)
#     tmp = sorted(tmp, reverse=True)
#     print(tmp)


# fhand = open('hello.py')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1

# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)
# for val, key in lst[:10]:
#     print(key, val)

# # below is the same thing as 334-336
# c = {'a':10,'b':1,'c':22}
# print( sorted( [ (v,k)for k, v in c.items() ] ) )

# x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
# y = x.items()
# print(y)


# names = ['mash', 'rashann', 'juan', 'andrea']
# print('names3=',names[3])
# print('names-4=',names[-4])
# names.append('churchwell')
# print('names',names)


# Try this:

# Add 'hamster' to the end of the list.
# Remove 'dog' from the list.
# Insert 'turtle' at index 1.


# Print the final list.
# animals = ['cat', 'dog', 'bird']
# print(animals.append('hamster'))
# # print(animals)
# # print(animals)
# print(animals.insert(0,'turtle'))
# #the next 2 lines do the same thing
# # print(animals.pop(1))
# print(animals.remove('dog'))
# print(animals)


# numbers = [3,7,2,9,4]
# for evens in numbers:
#     if evens % 2 == 0:
#         print(f'{evens} is even')
#     else:
#         print(f'{evens} is odd')

# numbersTakeTwo = [1,2,3,4,5,6,7,8,9]
# for odds in numbersTakeTwo:
#     if odds % 2 != 0:
#         print(f'its odd')
#     else: 
#         print(f'its even')


#if elif statements:


# age = 23

# if age >=21:
#     print('you can go to a bar')
# elif age >= 18:
#     print('you cant go to a bar, but you can vote')
# elif age == 16:
#     print('you can drive')
# else:
#     print('you cant do none of the above!!')



# toDoList = []
# toDoList.append('Study PYTHON')
# toDoList.append('Finish Homework')
# toDoList.append('Feed Louie')
# print('My current todolist', toDoList)

# compTask = toDoList.pop()


# class MyList:
#     def __init__(self, items):
#         self.items = items

#     def pop(self, index=None):
#         if not self.items:
#             raise IndexError("pop from empty list")
        
#         if index is None:
#             index = len(self.items) - 1  # Default to last item
        
#         if index < 0 or index >= len(self.items):
#             raise IndexError("pop index out of range")
        
#         popped_item = self.items[index]
        
#         # Shift elements to remove item at index
#         self.items = self.items[:index] + self.items[index+1:]
        
#         return popped_item



# print('completed', compTask)



# data = 'abcdefghijk'
# print(data.split(' , '))
# print(list(data))


# # Create an empty list to store tasks
# todo_list = []

# while True:
#     task = input("Enter a task (or type 'quit' to stop): ")
    
#     if task.lower() == "quit":
#         break  # Exit the loop if the user types "quit"
    
#     todo_list.append(task)
#     print(f"Task '{task}' added!")

# # Show the full to-do list
# print("\nYour To-Do List:")
# for i, item in enumerate(todo_list, 1):
#     print(f"{i}. {item}")


# 🧠 Basic Warm-Ups
# Count to 10
# Use a while loop to print numbers 1 through 10.

# Even Numbers Only
# Print only the even numbers from 1 to 20.

# Countdown
# Start at 10 and count down to 1. After the loop, print “Liftoff!”

# count = 1

# while count <= 10:
#     print(count)
#     count += 1
# print('blastoff')
    
# loops while and for!!

# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print('value is now equal to ' + str(value))


# bikes = ['honda', 'suzuki','yamaha','ducati', 'harley']

# for bike in bikes:
#     print(bike)

# for i in range(5):
#     print('iter==',i)

# count = 0

# while count < 5:
#     print(count)
#     count = count + 1


# number = 6
# if number % 2 == 0:
#     print('even')
# else: 
#     print('odd')



# conditional in a for loop that checks for something
# i wanna go thru a list of animals,
# if its, cats, then its the best,
# if not, thats cool too!!


# animals = ['cats', 'dogs', 'birds','fish']

# for animal in animals:
#     if animal == 'cat':
#         print(f'{animal} ARE THE BEST!!!!')
#     else:
#         print(f'{animal} is cool too.')


# for i in range(1,11):
#     if i % 3 == 1 and i % 5 == 2:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('buzz')
#     elif i % 2 == 0:
#         print('BUZZYYY')
#     else: print(i)


# create loop that takes a number and outputs evens


# while True:
#     userInput = input("Type a number that's even (or 'exit' to quit): ")
    
#     if userInput.lower() == 'exit':
#         break

#     if userInput.isdigit():
#         number = int(userInput)
#         if number % 2 == 0:
#             print(f"{number} is even!")
#         else:
#             print(f"{number} is not even.")
  
# """control flow determines the order in which statements are executed in a program. by default, python executes code sequentially, line by line. However, w control flow statements, we can change this sequence based on conditions"""
#the if statement is the simplest form of a conditional stmt. it allows you to execute a block of code only if a specified condition is true

    
# def is_positive(num):
#     if num > 0:
#         print(f'{num} is positive')
#     elif num == 0:
#         print(f'{num} is zero')
#     else:
#         print(f'{num} is negative.')
    
# is_positive(5)
# is_positive(0)
# is_positive(-3)

# def is_even_or_odd(num):
#     if num % 2 == 0:
#         print(f'{num} is even.')
#     else: 
#         print(f'{num} is odd')
# is_even_or_odd(4)
# is_even_or_odd(7)

#  Challenge #3: Simple Function with a Return Value
# Task: Write a function called max_of_two that takes two numbers and returns the larger of the two numbers.

# def max_of_two(num1, num2):
#     if num1 > num2:
#         return num1
#     else: 
#         return num2
# print(max_of_two(4,7))
# print(max_of_two(-1,-5))

# def abs_difference(num1, num2):
#     return abs(num1 - num2)
# print(abs_difference(5,3))
# print(abs_difference(-2,4))

# def compstr(str1, str2):
#     if str1 == str2:
#         return 'identical'
#     elif len(str1) != len(str2):
#         return 'diff length'
#     else:
#         return 'totally diff str'
    
# print(compstr('hello', "hello"))
# print(compstr('hello', "world"))
# print(compstr('hey', "world"))

# def startsWaVowel(str):
#     if str[0] in 'aeiouAEIOU':

#         return 'starts w vowel'
#     else:
#         return 'dont start w vowel'
    
# print(startsWaVowel('apple'))
# print(startsWaVowel('orange'))
# print(startsWaVowel('banana'))


    
    
# def checkEven(num):
#     if num % 2 == 0:
#         print(f'{num}, is even')
#     else:
#         print(f'{num} is odd')
    
# checkEven(2)
# checkEven(3)
# checkEven(4)
# checkEven(5)

# def printOddNums(numbers):
#     for odds in numbers:
#         if odds % 2 != 0:
#             print(f'{odds} is odd')
#         else:
#             print(f'{odds} is even')
# printOddNums([1,2,3,4,5])

# def getEvenNum(nums):
#     newList = []
#     for evens in nums:
#         if evens % 2 == 0 and evens > 3:
#             newList.append(evens)
#     return newList
        
# print(getEvenNum([1,2,3,4,5,6]))

     
# def geteven(num):
#     if num % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'

# takin in a list
# total_sum = []
# loop see if positive if so add to total sum and return total sum

# def possum(listNum):
#     total_sum = 0
#     counter = 0
#     for i in listNum:
#         if i > 0:
#             total_sum = total_sum + i
#             if i % 2 == 0:
#                 counter += 1


#     return total_sum, counter
# print(possum([-2,-3,2,1,2]))