# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json
# Sample JSON
userJSON = '{"first_name":"John", "last_name":"Doe", "age":30 }'
#parse Json
user = json.loads(userJSON)
print(user)