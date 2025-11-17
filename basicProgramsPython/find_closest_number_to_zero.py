from typing import List


class FindClosestNumber:

    def findClosestNumber(self, nums: List[int]) -> int:

        closest = nums[0]

        for x in nums:
            if abs(x) < abs(closest):
                closest = x

        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        

if __name__ == "__main__":
    findClosestNum = FindClosestNumber()
    print(findClosestNum.findClosestNumber([-20,-10,3,4,5,10]))

    # Output: 3 (longest sequence length 3,4,5)