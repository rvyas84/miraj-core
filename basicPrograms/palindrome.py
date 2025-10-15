class Palindrome:

    def isPalindrome(self, text):
        return text == text[::-1]

pal = Palindrome()
print(pal.isPalindrome("madam"))