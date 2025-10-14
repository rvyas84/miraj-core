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