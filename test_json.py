
import json

# JSON string
d = {'id': '09', 'name': 'khushbu', 'department': 'development'}
print("This is Python", type(d))

print("\nNow Convert from Python to JSON")

# Convert Python dict to JSON
obj = json.dumps(d, indent=4)
print("Converted to JSON", type(obj))
print(obj)