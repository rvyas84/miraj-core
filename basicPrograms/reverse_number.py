class ReverseNumber:
    """
    A class to reverse a given integer number.

    Methods
    -------
    revNumber(number: int) -> int:
        Reverses the digits of the given integer number and returns the reversed number.
    """
    
    def __init__(self):
        pass

    def revNumber(self, number):
        result = 0
        while not number == 0:
            result = (result * 10) + (number % 10)
            number = int(number / 10)
        
        return result

if __name__ == "__main__":
    revNum = ReverseNumber()
    print("Reversed number: ", revNum.revNumber(12345))
    print(f"Reversed Number: {revNum.revNumber(12345)}")
    print("Reversed number: {} ".format(revNum.revNumber(12345)))
        