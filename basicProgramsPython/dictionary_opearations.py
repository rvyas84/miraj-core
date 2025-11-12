"""
This script demonstrates various operations on dictionaries in Python.
It covers the following functionalities:

1. Creating dictionaries using curly braces and the dict() function.
2. Accessing dictionary items using square brackets and the get() method.
3. Modifying dictionary items by adding and updating key-value pairs.
4. Removing items from a dictionary using the del statement and the pop() method.
5. Iterating through dictionaries to access keys, values, and key-value pairs.

Example usage:
- Create a user data dictionary and manipulate it.
"""
# Create Dictionary Using Curly Braces

userData = {
    "firstName": "foo",
    "lastName": "Bar",
    "Age": 40,
    "zipcode": 12345
}

print("Curly Brace Dictionary: ", userData)

# Create Dictionary Using dict() keyword

userData1 = dict(firstName = "Bob", lastName = "Slice", age = 45, zicode = 56789)
print("Using dict() function: ", userData1)

#Accessing Dictionary Items using square bracket
name = userData["firstName"]
print("UserData name: ", name)

#Accessing Dictionary Items using get()
age = userData1.get("age")
print(age)

#Modifyin Dictionary Items

userData["graduationYear"] = 2020
userData["Age"] = 22

print(userData)

# Removeing from Dictionary Using del

del userData["graduationYear"]
print(userData)

userData.pop("Age")
print(userData)

# Iterating through Dictionary

for key in userData1:
    print("Keys:", key, userData1[key])

# Iterating through values

for value in userData1.values():
    print("Vaues: ", value)

# Iterating through Key-Value pair:
for key, value in userData1.items():
    print("Key:Value: ", key, value)