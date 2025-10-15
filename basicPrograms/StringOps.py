"""
This script demonstrates various string operations in Python.

1. Initializes a test string and prints it.
2. Shows different ways to format and print the string.
3. Extracts and prints a substring from the string.
4. Reverses the string and prints it.
5. Accesses and prints a specific character from the string.
6. Converts the string to a list, inserts a character, and prints the modified list.
7. Prints a specific character from the original string.
8. Prints a substring using negative indexing.
9. Counts and prints the occurrences of a substring within a string starting from a specific index.
"""
testString = "Hello World"
print("Test String Value: ", testString)

print(f"Test String Value using Format: {testString}")

print("Test String Value Using .Format function : {}".format(testString))

print(testString[2:]) # prints substring starting index 2 to end of string

print(testString[::-1]) #Reverse The String

print(testString[6]) # Prints character at Index 6

l1 = list(testString)

l1.insert(6, "w")

print(l1)

print(testString[6])
print(testString[-8:])

st = "Hello Hello Hello He"

print("Occurrences of \"He\" in -- {} -- is: {}".format(st, st.count("He", 7)))