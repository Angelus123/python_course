# A List is a collection which is ordered and changeable. Allows duplicate members.
# create list
numbers =[1,2,3,4,5]
fruits = ['Apples', 'Orange', 'Grapes', ]
#use a constructor
# numbers2 =list((1,2,3,4,5))
# print (numbers, numbers2)

# Get a value 
print (fruits[1])
# Get length
print(len(fruits))
# Append to list
fruits.append ('Mangos')
# Remove from list
fruits.remove('Grapes')
# Insert into position
fruits.insert(2, 'Strawberries ')
# Change value
fruits[0] = 'Blueberries'
# Remove with pop
fruits.pop(2)
#Reverse list
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)

