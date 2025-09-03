

# def two_counts(nums):
#     avg = sum(nums) / len(nums)
#     above = 0
#     below_or_equal = 0
#     for num in nums:
#         if num > avg:
#             above +=1
#         else:
#             below_or_equal += 1
#     return above, below_or_equal
# print(two_counts([1, 2, 3, 4, 5, 6]))



# def split_by_average(nums):
#     avg = sum(nums) / len(nums)
#     above = []
#     below_or_equal = []
#     for num in nums:
#         if num > avg:
#             above.append(num)
#         else:
#             below_or_equal.append(num)
#     return above, below_or_equal
# print(split_by_average([1, 2, 3, 4, 5, 6]))



# def farthest_from_average(nums):
#     avg = sum(nums) / len(nums)
#     farthest = None
#     max_distance = 0

#     for num in nums:
#         # figure out how far this num is from avg
#         distance = abs(num - avg)
#         # update farthest if distance is bigger
#         if distance > max_distance:
#             farthest = num
#             max_distance = distance
#     return farthest


# print(farthest_from_average([1, 2, 3, 4, 5, 6]))

# def revSt(str):
#     return str[::-1]
# print(revSt('hello'))

# def removeD(l):
#     return list(set(l))
# print(removeD([1,2,2,3,3,3]))

# def remove_dup(nums):
#     clean = []
#     for num in nums:
#         if num not in clean:
#             clean.append(num)
#     return clean
# print(remove_dup([1,2,2,3,3,3]))

# def find_min_max(nums):
#     # start with the first number as both min and max
#     smallest = nums[0]
#     largest = nums[0]
#     for num in nums:
#         # if num is smaller than smallest, update smallest
#         if num < smallest:
#             smallest = num
#         # if num is bigger than largest, update largest
#         elif num > largest:
#             largest = num
#     return smallest, largest
# print(find_min_max([4, 2, 9, 7]))



# def reverse_string(s):
#     result = ""
#     for ch in s:
#         # put ch at the FRONT of result each time
#         print('ch==', ch)
#         result = ch + result
#     return result
# print(reverse_string("dog"))


# def count_vowels(s):
#     vowels = "aeiou"
#     count = 0
#     for ch in s:
#         if ch in vowels:
#             count +=1
#     return count
# print(count_vowels("hello"))

   
# def first_repeat(s):
#     seen = set()
#     for ch in s:
#         # check if we've seen this character already
#         if ch in seen:
#             return ch
#         else:
#             seen.add(ch)
#     return None


# print(first_repeat("letter"))
# print(first_repeat("python"))


# def remove_spaces(s):
#     result = ""
#     for ch in s:
#         # only add ch if it's not a space
#         if ch != " ":
#             result = result + ch
#     return result
# print(remove_spaces("hello world"))        


           
# def count_spaces(s):
#     count = 0

#     for ch in s:
#         # check if it's a space
#         if ch == ' ':
#             count += 1
#     return count
# print(count_spaces("hi there you"))


# def remove_vowels(s):
#     vowels = "aeiou"
#     result = ""
#     for ch in s:
#         # if ch is NOT a vowel, add it to result
#         if ch not in vowels:
#             result = result + ch
#     return result
# print(remove_vowels("hello world"))


# def square_list(nums):
#     result = []
#     for num in nums:
#         result.append(num * num)
#     return result
# print(square_list([1, 2, 3, 4]))


# def filter_evens(nums):
#     result = []
#     for num in nums:
#         # check if num is even
#         if num % 2 == 0:
#             result.append(num)
#     return result
# print(filter_evens([1, 2, 3, 4, 5, 6]))


# def sum_odds(nums):
#     total = 0

#     for num in nums:
#         # check if num is odd
#         if num % 2 != 0:
#             total += num

#     return total
# print(sum_odds([1, 2, 3, 4, 5]))



# def average(nums):
#     # add all numbers
#     # divide by how many numbers
#     avg = sum(nums) / len(nums)

#     return avg

# print(average([2, 4, 6, 8]))


# def average_odds(nums):
#     total = 0
#     count = 0

#     for num in nums:
#         # check if odd
#         if num % 2 != 0:
#             total += num
#             count += 1

#     # avoid division by zero
#     if count == 0:
#         return None
#     return total / count
# print(average_odds([1, 2, 3, 4, 5]))


# nums = [1, 2, 3, 4, 5]
# def looper(nums):
#     sum = 0
#     for num in nums:
#         # print('num===', num)
#         if num % 2 != 0:
#             sum += num
#     return sum
# print(looper(nums))


# my_str = 'volunteers'
# print(my_str[::-1])

# name = 'andrea'
# # print(name.title())
# print(name[0].upper() + name[1:])


# nums = [3, 7, 11, 3, 7, 15]
# # print each unique number (no repeats)
# print(list(set(nums)))


# nums = [3, 7, 11, 3, 7, 15]
# # print each unique number in the order they appear
# def uniques(nums):
#     seen = []
#     for num in nums:
#         if num not in seen:
#             seen.append(num)
#     return seen
# print(uniques(nums))


# numbers = [12, 5, 9, 20]
# # loop through and print "even" or "odd" for each number
# def even_odd(numbers):
#     for num in numbers:
#         if num % 2 == 0:
#             print(f'{num} is even')
#         else:
#             print(f'{num} is odd')
  
# even_odd(numbers)

# player = {"name": "LeBron", "team": "Lakers", "ppg": 25, "championships": 4}
# # print "Superstar" if ppg is 20 or higher, otherwise "Role player"
# print(player)
# def is_star(player):
#     if player['ppg'] >= 20:
#         return 'superstar'
#     else:
#         return 'role player'
    
# print(is_star(player))

# player = {'Name': 'Lebron James','team': 'Lakers', 'ppg': 25 }
# player['Rings'] = 4
# print(player)


# players = [
#     {"name": "LeBron", "ppg": 25, "team": "Lakers"},
#     {"name": "Curry", "ppg": 30, "team": "Warriors"},
#     {"name": "Dillon", "ppg": 12, "team": "Rockets"}
# ]
# def analyze_players(players):
#     for player in players:
#         print(player['name'].upper())
#         if player['ppg'] >= 20:
#             print(f"{player['name']} is a superstar!")
#         else:
#             print(f"{player['name']} is a role player!")
# analyze_players(players)
        

# players = [
#     {"name": "LeBron", "ppg": 25, "team": "Lakers"},
#     {"name": "Curry", "ppg": 30, "team": "Warriors"},
#     {"name": "Dillon", "ppg": 12, "team": "Rockets"}
# ]

# def s_or_r(players):
#     superstars = []
#     rolePlayers = []
#     for player in players:
#         if player['ppg'] >= 20:
#             superstars.append(player['name'])
#         else:
#             rolePlayers.append(player['name'])
#     return superstars, rolePlayers
# # unpack the two lists
# superstars, rolePlayers = s_or_r(players)

# # format nicely using join
# print("Superstars:", ", ".join(superstars))
# print("Role players:", ", ".join(rolePlayers))

# fruits = ["apple", "banana", "orange"]
# print(fruits)  
# print(', '.join(fruits))
# print(' - '.join(fruits))
# print(' *** '.join(fruits))

# players = [
#     {"name": "LeBron", "ppg": 25, "team": "Lakers"},
#     {"name": "Curry", "ppg": 30, "team": "Warriors"},
#     {"name": "Dillon", "ppg": 12, "team": "Rockets"}
# ]

# def get_roster(players):
#     result = []
#     for player in players:
#         result.append(player['name'])
#     return result
# # get the list of names
# names = get_roster(players)

# # join them into one string
# print("Team roster: " + ", ".join(names))
