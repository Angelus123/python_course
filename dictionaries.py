# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# Create dict
person = {
     'first_name': 'John',
     'last': 'Doe',
     'age':50
 }
#Use constructor
person2 = dict(firstname='Sara', last_name ='Williams')
# print(person2)
#Get value
# print(person['first_name']) 
# print(person2.get('last_name'))
#Add key/value  
person['phone'] = '555-555-5555'
# print(person['phone'])
#Get dict keys 
# print(person.keys())
#Get dict keys
# print(person.keys())

#Get dict items
# print(person.items())
# Copy dict
person2 =person.copy()
person2['city'] ='Boston'
#Remove item 
del(person2['age'])
person.pop('phone')
# clear
person.clear() 
print(person)                                                                                                                                                                      

# list of dict
people = [
    {'name':'Martha', 'age': 30},
    {'name':'kevin', 'age':25}
]
print(len(people))
print(people)

