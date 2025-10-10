class ReverseNumber:
    
    def __init__(self):
        pass

    def revNumber(self, number):
        result = 0
        while not number == 0:
            result = (result * 10) + (number % 10)
            number = int(number / 10)
        
        return result

revNum = ReverseNumber()
print("Reversed number: ", revNum.revNumber(12345))
print(f"Reversed Number: {revNum.revNumber(12345)}")
print("Reversed number: {} ".format(revNum.revNumber(12345)))
    