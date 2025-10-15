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