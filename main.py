import methods
import map
import UsableMap
import math


#ask someone what they know (vertical displacement, horizontal displacement, time, initial vertical velocity, final vertical velocity, horizontal velocity)

print("From this list of categories (vertical displacement, horizontal displacement, time, initial vertical velocity, final vertical velocity, horizontal velocity)")

#create empty list of known variables and their corresponding categories
knownDict = {}

#ask the user what they are looking for and store in a dictionary
key = input("What are you trying to find: ")
value = "unknown"
knownDict[key] = value

#if they type in an unusable category exit
try:
    usableC = UsableMap.usableMapping[key]
except:
    print('That is not a valid category')
    exit(0)

#get the possible known combinations and tell the user
#take two inputs of category and value from user and store them in a dictionary

print(f"You can find this by using {usableC}")
for i in range(2):

    key = input("Type in a known category: ")
    value = float(input("Type in the value: "))
    knownDict[key] = value 


#get the categories for the if statements
categories = list(knownDict.keys())
reverseC = [categories[0], categories[2], categories[1]]

#if statements to match



print(knownDict)

if tuple(categories) in map.functionMapping:
    output = map.functionMapping[tuple(categories)](knownDict[categories[1]], knownDict[categories[2]])
    print(output)
elif tuple(reverseC) in map.functionMapping:
    output1 = map.functionMapping[tuple(reverseC)](knownDict[categories[2]], knownDict[categories[1]])
    print(output1)
else:
    print("this is not a category combination")






#set up a dictionary 

