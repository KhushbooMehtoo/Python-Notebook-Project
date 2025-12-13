
import json

my_json ='{"name":"Khushboo","age":"20","Department":"Development"}'

my_py=json.loads(my_json)

print("convert JSON String into Python Dictionary")
print(my_py)



#converting python dictionary into json

my_p={
    "name":"khushboo",
    "age":"20"
}
print("convert Python  Dictionary INTO json String ")
my_j=json.dumps(my_p)
print(my_j)


# #JSON String
# emp='{"id":"01","emp_name":"Khushboo","department":"Development"}'
# print("This is JSON String",type(emp))

# #convert into python 
# print("Convert From Json to Python")

# #convert string itno dictionary
# my_emp= json.loads(emp)
# print("convert into python",type(my_emp))
# print(my_emp)



# ******************************........

# JSON string
# d = {'id': '09', 'name': 'khushbu', 'department': 'development'}
# print("This is Python", type(d))

# print("\nNow Convert from Python to JSON")

# # Convert Python dict to JSON
# obj = json.dumps(d, indent=4)
# print("Converted to JSON", type(obj))
# print(obj)