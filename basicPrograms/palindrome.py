class Palindrome:

    def isPalindrome(text):
        return text == text[::-1]

pal = Palindrome
print(pal.isPalindrome("madam"))