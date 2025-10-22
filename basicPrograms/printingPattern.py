for i in range(4):
    for j in range(4):
        print("# ",end="")
    print()

# # # # 
# # # # 
# # # # 
# # # # 

print()

for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()

# # # # 
# # # 
# # 
# 

print()

for i in range(4):
    for j in range(i+1):
        print("# ",end="")
    print()

# 
# # 
# # # 
# # # # 

print("Pyramid")

for i in range(1, 5 + 1):
        # Print leading spaces
        print(" " * (5 - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

#     *
#    ***
#   *****
#  *******