# myDict = {
#     'name': 'andrea',
#     'age': 43,
#     'pet': 'louie'

# }
# print(myDict['pet'])
# myDict['favDay'] = 'Saturday'
# myDict['favDay'] = 'Sunday'
# del myDict['age']
# print(myDict)

nestedD = {
    'k1':{
        'name': 'andrea',
        'age': 43
    },
    'k2':{
        'name': 'pam',
        'age': 67
    }
}
nestedD['k1']['name']
nestedD['k2']['age']
print(nestedD['k1'])
print(nestedD['k2'])
nestedD['k1']['hobby'] = 'outdoors'
nestedD['k2']['hobby'] = 'shopping'
nestedD['k1']['age'] = 42
del nestedD['k2']['age']

nestedD['k1']['hobby'] ='coding'
print(nestedD)
