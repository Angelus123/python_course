# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
# Create class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
        def set_balance(self, balance):
            self.balance =balance 
        
    def greeting(self): 
        return f'My name is {self.name} and I am {self.age}'
    def has_birthday (self):
        self.age +=1

#Extend class
class Customer (User):
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance (self, balance):
        self.balance = balance
    def greeting(self): 
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#Init user object
brad = User('Janet Jonson', 'janet@yahoo.com', 25)
print(type(brad)) 

# Init Customer object
janet = Customer('Janet Jonson', 'janet@yahoo.com', 25)
janet.set_balance(500)
brad.has_birthday()
print(brad.greeting())
print(janet.greeting())