from typing import List

class LongestSequence:

    def findLongestSequence(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest
    

if __name__ == "__main__":
    longestSeq = LongestSequence()
    print(longestSeq.findLongestSequence([100,4,200,1,3,2,201,202,203,204,205]))

# Output: 6 (longest sequence count: 200,201,202,203,204,205)