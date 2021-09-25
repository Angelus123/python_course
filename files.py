# Python has functions for creating, reading, updating, and deleting files.
# Open a file
myFile = open('myfile.txt', 'w' )
#Get some info
print('name:', myFile.name)
print ('Is closed:', myFile.closed)
print('Opening Mode:', myFile.mode)
myFile.write("I love Python")
myFile.write(' and Javascript')
myFile.close()
myFile =open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()
myFile = open('myfile.txt', 'r' )
text =myFile.read(100)
print(text)