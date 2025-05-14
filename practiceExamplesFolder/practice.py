# text = 'Hello, world!'
# print(text[1:5])
# print(text[-6])
# print(text[::5])

# for items in text:
#     print(items)

# def rev(str):
#     reversed = ''
#     for items in str:
#         reversed = items + reversed
#     return reversed
# print(rev('Hello'))

# def backwards(str):
#     result = ''
#     for item in str:
#         result = item + result
#     return result
# print(backwards('andrea'))

# numbers = [5, 12, 18, 3, 7, 22, 10, 15]
# newlist = []
# for item in numbers:
#     if item % 2 == 0 and item > 10:
#         newlist.append(item)

# print(newlist)

# def find_max_min(numbers):
#     maxV = max(numbers)
#     minV = min(numbers)
#     return maxV, minV
# numbers = [5, 12, 18, 3, 7, 22, 10, 15]
# result = find_max_min(numbers)
# print(result)

# cart = [10,20,39]
# total = 0
# for item in cart:
#     total = total + item
# print(total)
# numbers = [2,5,2,7,10]
# max = numbers[0]
# for item in numbers:
#     if item > max:
#         max = item
# print(max)

# biggie = [23,55,77,54,88,56]
# big = biggie[0]
# for item in biggie:
#     if item > big:
#         big = item
# print(big)

        

# numb = [2,2,2,3,4,5,66,2,1]
# uniques = []
# for num in numb:
#     if num not in uniques:
#         uniques.append(num)
# print(uniques)

       
# dogs = {
#     "Louie": {
#         "breed": "Tabby (ok, he's a cat!)",
#         "age": 5,
#         "likes": ["naps", "treats", "windowsills"]
#     },
#     "Buddy": {
#         "breed": "Golden Retriever",
#         "age": 3,
#         "likes": ["fetch", "belly rubs", "swimming"]
#     },
#     "Luna": {
#         "breed": "Husky",
#         "age": 4,
#         "likes": ["howling", "running", "snow"]
#     }
# }
# print(dogs.get('Louie','breed'))

# playlist = {
#     "title": "Feel Good Vibes",
#     "songs": [
#         {"title": "Sunshine", "artist": "Kygo"},
#         {"title": "Good Day", "artist": "ZHU"},
#         {"title": "Happy Place", "artist": "Jax Jones"}
#     ],
#     "owner": {
#         "username": "acodequeen",
#         "location": "Selmer, TN"
#     }
# }
# print(playlist.get('title'))
# print(playlist.get("songs")[1].get("artist"))
# print(playlist.get('owner').get('location'))


# pets = {
#     "Louie": {
#         "type": "Cat",
#         "age": 5,
#         "favorite_things": ["sunbeams", "treats", "being fabulous"]
#     },
#     "Max": {
#         "type": "Dog",
#         "age": 2,
#         "favorite_things": ["bones", "running", "cuddles"]
#     },
#     "Bella": {
#         "type": "Rabbit",
#         "age": 3,
#         "favorite_things": ["carrots", "digging", "hopping"]
#     }
# }
# print(pets.get('Louie').get('age'))
# print(pets.get('Bella').get('favorite_things')[1])
# print(pets.get('Max').get('type'))

# movies = {
#     "The Matrix": {
#         "year": 1999,
#         "genre": "Sci-Fi",
#         "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]
#     },
#     "The Lion King": {
#         "year": 1994,
#         "genre": "Animation",
#         "cast": ["Matthew Broderick", "James Earl Jones", "Jeremy Irons"]
#     },
#     "Hidden Figures": {
#         "year": 2016,
#         "genre": "Drama",
#         "cast": ["Taraji P. Henson", "Octavia Spencer", "Janelle Monáe"]
#     }
# }
# print(movies.get('Hidden Figures').get('genre'))
# print(movies.get('The Matrix').get('cast')[0])
# print(movies.get('The Lion King').get('year'))

# def revSt(str):
#     result = ''
#     for i in str:
#         result = i + result
#     return result

# print(revSt('hello'))

# def firstthree(word):
#     first_part = word[:3]  # First 3 letters
#     rest_part = word[3:]   # Everything after the first 3
#     reversed_first = first_part[::-1]  # Reverse the first 3
#     return reversed_first + rest_part  # Put them together

# print(firstthree('hello'))

# def looper(num):
#     count = 0
#     while num <= 5:
#         return count
# print(looper(5))


# def loop(str):
#     result = ''
#     for i in str:
#         print('i==', str, 'res==', result)
#         result = i + ' '
#         for j in str:
#             print('j===', j, 'res==', result)
#     return result

# print(loop('andreachurchwell'))

# practice how many vowels are in a given String 
# take a str input 
# loop thru chars
# check if its a vowel
# return total num of vowels
 
# def vowelCount(input_str):
#     count = 0
#     vowels = 'aeiouAEIOU'
#     for i in input_str:
#         # print(i)
#         if i in vowels:
#             count += 1
#     return count
# print(vowelCount('andrea'))

#  Practice Task: Reverse Words in a Sentence
# Goal: Write a function that takes a sentence and returns a new sentence where each word is reversed, but the word order stays the same.

# Define a function called reverse_words(sentence).

# Split the sentence into words.

# Reverse each word individually.

# Rejoin the reversed words into a single string, with spaces in between.


# def reverse_words(sentence):
#     words = sentence.split(' ')
#     revWord = []
#     for word in words:
#         # print('word', word)
#         revWord.append(word[::-1])
#     return ' '.join(revWord)


# print(reverse_words('hello my name is andrea'))


# def revS(sent):
#     reversedS = sent.split(' ')
#     result = []
#     for words in reversedS:
        
#         result.append(words[::-1])
#     return ' '.join(result)

# print(revS('hi my name is'))


# listOfNum = [1,2,3,4,5]
# print(listOfNum[0])
# print(listOfNum[-1])

# str = 'Hello, how are you today?'
# def howMany(str):
#     count = 0
#     for word in str.split():
#         if word == 'how':
#             count +=1
#     return count
# print(howMany('Hello, how are you today?'))

# def allEven(numbs):
#     result = []
#     for even in numbs:
#         if even % 2 == 0:
#             result.append(even)
#     return result
# print(allEven([1,2,3,4,5,6,7,8,9,10]))


# def numCkr(numbs):
   
#     if numbs == 0:
#          print(f'{numbs} is zero')
#     elif numbs > 0:
#             print(f'{numbs} is positive')
#     else:
#         print(f'{numbs} is negative')
# print(numCkr(0))
# print(numCkr(10))
# print(numCkr(-20))

# def numCkr(numbs):
#     for num in numbs:
#         if num == 0:
#             print(f'{num} is zero')
#         elif num > 0:
#             print(f'{num} is positive')
#         else:
#             print(f'{num} is negative')

# numCkr([0, 10, -20, 15, -5])

# def getsum(num1,num2):
#     return num1 + num2
# print(getsum(5,5))


# def sumOfList(nums):
#     sum = 0
#     for i in nums:
#         sum += i
#     return sum
# print(sumOfList([1,2,3]))

# def countV(s):
#     count = 0
#     for l in s:
#         if l in 'aeiouAEIOU':
#             count += 1
#     return count
# print(countV('hello'))


# def maxV(nums):
#     biggestNum = nums[0]
#     for num in nums:
#         if num > biggestNum:
#             biggestNum = num
#     return biggestNum
# print(maxV([1,2,3,4]))
    
    


# def smallest(nums):
#     smallestVal = nums[0]
#     for num in nums:
#         if num < smallestVal:
#             smallestVal = num
#     return smallestVal
# print(smallest([1,2,3,4]))


# def hasDupes(nums):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):  # Compare each element with all others after it
#             if nums[i] == nums[j]:
#                 return True  # Duplicate found, return True
#     return False  # No duplicates found, return False

# print(hasDupes([1, 1, 2, 3, 4]))  # Should return True (duplicate found)
# print(hasDupes([1, 2, 3, 4]))     # Should return False (no duplicates)

# def isPal(word):
   
#     if word  == word[::-1]:
#         return f'{word} is a pal'
#     else:
#         return f'{word} is not a pal'
    

# print(isPal('hello'))
# print(isPal('level'))


# this one is my solution
# def greaterThanAvg(numbers):
#     newList = []

#     for num in numbers:
#         if num > sum(numbers) / len(numbers):
#             newList.append(num)
#     return newList

# print(greaterThanAvg([1,2,3,4]))


# # below chatgpt said would be better
# def greaterThanAvg(numbers):
#     avg = sum(numbers) / len(numbers)  # Calculate average once
#     newList = []
#     for num in numbers:
#         if num > avg:
#             newList.append(num)
#     return newList

# print(greaterThanAvg([1, 2, 3, 4]))



# def longlist(listOfStr):
#     longestSofar = listOfStr[0]
#     for item in listOfStr:
#         if len(item) > len(longestSofar):
#             longestSofar = item
#     return longestSofar

# print(longlist(['apple', 'banana', 'cherry', 'kiwi']))  


# def sumEven(numbs):
#     sum = 0
#     for num in numbs:
#         if num % 2 == 0:
#             sum += num
#     return sum
# print(sumEven([1,2,3,4,5,6]))


# def ktok(n, k):
#     if k**k == n:
#         return True
#     else:
#         return False



# print(ktok(4, 2))  # 2**2 = 4 → matches → True
# print(ktok(387420489, 9)) # 9**9 = 387420489 → matches → True
# print(ktok(3124, 5))  # 5**5 = 3125 ≠ 3124 → False
# print(ktok(17, 3))  # 3**3 = 27 ≠ 17 → False


# def countUpperCase(str):
#     count = 0
#     for i in str:
#         if i.isupper():
#             count += 1
#     return count
# print(countUpperCase('ANdreA'))


# def countShortWds(words):
#     count = 0
#     for word in words.split():
#         if len(word) <= 4:
#             count += 1
#     return count

# print(countShortWds('The fox is in the den'))

# sentences = [
#     "The cat sat on the mat.",
#     "The dog barked at the cat.",
#     "The cat ran away from the dog."
# ]



# words = ["apple", "banana", "apricot", "blueberry", "cherry"]
# def groupByfirstLetter(words):
#     result = {}
#     for word in words:
#         firstLetter = word[0]
#         if firstLetter not in result:
#             result[firstLetter] = []
#         result[firstLetter].append(word)
#     return result


# print(groupByfirstLetter(words))

# def wordGroup(words):
#     result = {}
#     for word in words:
#         length = len(word)
#         if length not in result:
#             result[length] = []  # Create an empty list for new lengths
#         result[length].append(word)  # Add the word to the correct list
#     return result

# words = ["apple", "banana", "pear", "grape", "kiwi", "peach"]

# def groupbylen(words):
#     result = {}
#     for word in words:
#         lengthOfW = len(word)
#         if lengthOfW not in result:
#             result[lengthOfW] = []
#         result[lengthOfW].append(word)
#     return result
# print(groupbylen(["apple", "banana", "pear", "grape", "kiwi", "peach"]))

# def freqC(listOfWords):
#     result = {}
    
#     for word in listOfWords:
#         if word not in result:
#             result[word] = 1
#         else:
#             result[word] += 1
#     return result
# print(freqC(["apple", "banana", "apple", "kiwi", "banana", "kiwi", "kiwi"]))


# books = [
#     ("The Catcher in the Rye", 10.99),
#     ("1984", 8.99),
#     ("To Kill a Mockingbird", 12.99),
#     ("The Great Gatsby", 9.99),
#     ("Moby Dick", 14.99)
# ]

# # result = books[::-1]
# # print(result)

# bookPrices = {}
# for book in books:
#     title = book[0]
#     price = book[1]
#     bookPrices[title] = price
# print(bookPrices)

# totalSum = 0
# for price in bookPrices.values():
#     totalSum += price
# numberOfBooks = len(bookPrices)
# avgPrice = totalSum / numberOfBooks
# print(f"The average price is: {avgPrice}")
    

people = [
    ("Alice", 17),
    ("Bob", 23),
    ("Charlie", 35),
    ("David", 45),
    ("Eve", 52),
    ("Frank", 12),
    ("Grace", 30),
    ("Hannah", 60)
]
ageGroups = {
    'over 50': [],
    '36-50': [],
    '18-35': [],
    'under18': []
}   
for name,age in people:
    if age < 18:
        ageGroups['under18'].append(name)
    elif 18 <= age <= 35:
        ageGroups['18-35'].append(name)
    elif 36 <= age <= 50:
        ageGroups['36-50'].append(name)
    else:
        ageGroups['over 50'].append(name)

# Print the result
print(ageGroups)   
    

