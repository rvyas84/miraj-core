class FindLongestPalindromeSubString:
    """
    A class to find the longest palindromic substring in a given string.

    Methods
    -------
    findSubStringPalindrome(s: str) -> str:
        Returns the longest palindromic substring in the input string.

    expandFromMiddle(s: str, top: int, bottom: int) -> int:
        Expands around the center indices to find the length of the palindrome.
    """
    
    def findSubStringPalindrome(self, s):
        top = 0
        bottom = 0

        if s == "" or len(s) < 1:
            return ""
        
        for c in range(len(s)):
            len1 = self.expandFromMiddle(s, c, c)
            len2 = self.expandFromMiddle(s, c, c+1)

            resultLen = max(len1, len2)

            if resultLen > (bottom - top):
                top = int(c - (resultLen - 1)/2)
                bottom = int(c + (resultLen)/2)

        return s[top : bottom + 1]    

    def expandFromMiddle(self, s, top, bottom):
        if (s == "" or bottom > top):
            return 0

        while (top >= 0 and bottom < len(s) and s[top] == s[bottom]):
            top -= 1
            bottom += 1
        
        return bottom - top - 1
    
pali = FindLongestPalindromeSubString()
print(pali.findSubStringPalindrome("racecar"))
