import math

class CalculateFactorial:

    def __init__(self):
        pass
        
    def calculateFactorial(self, n):
        if n < 0:
            print("Factorial is not defined for negative number")
        elif n == 0 or n == 1:
            return 1
        else:
            return n * self.calculateFactorial(n-1)


calc = CalculateFactorial()
print(calc.calculateFactorial(5))

# Using Math Factorial Function
print(math.factorial(5))

print("The factorial of -5 is ", end = "")

# raises exception
print(math.factorial(-5))

# 120
# 120
# The factorial of -5 is Traceback (most recent call last):
#   File "/Users/rajanvyas/miraj-core/basicPrograms/factorial.py", line 26, in <module>
#     print(math.factorial(-5))
#           ~~~~~~~~~~~~~~^^^^
# ValueError: factorial() not defined for negative values

# Exceptions ( Non-Integral number )
print("The factorial of 5.6 is : ", end="")

# raises exception
print(math.factorial(5))

# The factorial of 5.6 is : Traceback (most recent call last):
#   File "/Users/rajanvyas/miraj-core/basicPrograms/factorial.py", line 40, in <module>
#     print(math.factorial(5.6))
#           ~~~~~~~~~~~~~~^^^^^
# TypeError: 'float' object cannot be interpreted as an integer