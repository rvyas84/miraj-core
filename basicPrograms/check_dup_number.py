from typing import List

class FindDupNumber:

    def checkDuplicate(self, nums: List[int]) -> bool:
        
        for number in range(len(nums)):
            for num in range(number + 1, len(nums)):
                if nums[number] == nums[num]:
                    return True
        return False
    
    def checkDupWithSets(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
    def checkDupWithDict(self, nums: List[int]) -> bool:
        result = {}

        for num in nums:
            result[num] = result.get(num, 0) + 1
            if result[num] > 1:
                return True
        return False
    
if __name__ == "__main__":
    findDup = FindDupNumber()
    print(findDup.checkDuplicate([1,2,3,4,5,6,7,8,9,3])) # True
    print(findDup.checkDupWithSets([1,2,3,4,5,6,7,8,9])) # False
    print(findDup.checkDupWithDict([1,2,3,4,5,6,7,8,9])) # False