import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
obj2 = json.loads(x)
print(obj2["city"])

