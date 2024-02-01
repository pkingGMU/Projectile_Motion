import methods
import map

#ask someone what they know (vertical displacement, horizontal displacement, time, initial vertical velocity, final vertical velocity, horizontal velocity)

print("From this list of categories (vertical displacement, horizontal displacement, time, initial vertical velocity, final vertical velocity, horizontal velocity)")

#create empty list of known variables and their corresponding categories
knownDict = {}

#take two inputs of category and value from user and store them in a dictionary
for i in range(2):

    key = input("Type in a known category: ")
    value = int(input("Type in the value: "))
    knownDict[key] = value 

    if i !=0:
        key = input("What are you trying to find: ")
        value = "unknown"
        knownDict[key] = value

#get the categories for the if statements
categories = list(knownDict.keys())
reverseC = [categories[1], categories[0], categories[2]]

#if statements to match



print(knownDict)
print(categories)

if tuple(categories) in map.functionMapping:
    output = map.functionMapping[tuple(categories)](knownDict[categories[0]], knownDict[categories[1]])
    print(output)
elif tuple(reverseC) in map.functionMapping:
    output1 = map.functionMapping[tuple(reverseC)](knownDict[categories[1]], knownDict[categories[0]])
    print(output1)
else:
    print("this is not a category combination")






#set up a dictionary 

