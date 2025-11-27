from typing import List

class ProductArrayExceptSelf:

    def productArray(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result


if __name__ == "__main__":
    productArray = ProductArrayExceptSelf()
    print(productArray.productArray([2,3,4,5,6]))

#Output: [360, 240, 180, 144, 120]