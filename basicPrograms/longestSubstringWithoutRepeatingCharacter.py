# def findLongestSubStringWithoutRepeatingCharacter(str):
#     top = 0
#     bottom = 0
#     chars = set()
#     maximum = 0

#     while bottom in range(len(str)):
#         if not str[bottom] in chars :
#            chars.add(str[bottom])
#            bottom += 1
#            maximum = max(len(chars), maximum)
#         else:
#             chars.remove(str[top])
#             top += 1
        
#     return maximum


# print(findLongestSubStringWithoutRepeatingCharacter('abcda'))


class Solution:
    def lengthOfLongestSubstring(self, str):
        top = 0
        bottom = 0
        chars = set()
        max_length = 0

        while bottom in range (len(str)):
            if not str[bottom] in chars:
                chars.add(str[bottom])
                bottom += 1
                max_length = max(len(chars), max_length)
            else:
                chars.remove(str[top])
                top += 1
        
        return max_length

sol = Solution()
print(sol.lengthOfLongestSubstring("abcdefabcbb"))