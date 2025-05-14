# listOfNums = [1,2,3,4,5,6,7,8,9,10]
# print(listOfNums[0])
# print(listOfNums[-1])
# print(listOfNums[2])
# listOfNums[4] = 99
# listOfNums[-1] = 50
# listOfNums.append(11)
# listOfNums.remove(7)
# listOfNums[:3]
# print(listOfNums[:3])

# print(sum(listOfNums))
# print(sum(listOfNums)/ len(listOfNums))

# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# dby3 =[x for x in nums if x % 3 == 0]
# print(dby3)
# sqL = [x**2 for x in nums if x > 5]
# print(sqL)

def numbCounter(nums):
    evens = 0
    odds = 0
    result = {}
    for items in nums:
        if items % 2 == 0:
            evens += 1
        else:
            odds +=1
    result['odds'] = odds
    result['evens'] = evens
    return result

print(numbCounter([1,2,3,4,5,6,7,8,9,10]))