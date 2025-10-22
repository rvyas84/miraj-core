class Palindrome:
    """
    A class to check if a given string is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters
    that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    """

    def isPalindrome(self, text):
        return text == text[::-1]

pal = Palindrome()
print(pal.isPalindrome("madam"))

def pali(testData):
    lenData = len(testData)
    for i in range(lenData // 2):
        if testData[i] != testData[lenData - i - 1]:
            return False
    return True
        
print(f"Pali Test 1 - {'racecar'} : {pali('racecar')}")  # True