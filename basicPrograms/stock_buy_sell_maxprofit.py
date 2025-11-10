from typing import List

class StockBuySell:
    def stockBuySell(self, nums: List[int]) -> int:
        l = 0 #buy
        r = 1 #sell
        maxProfit = 0
        
        while r < len(nums):
            if nums[l] < nums[r]:
                profit = nums[r] - nums[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1

        return maxProfit


if __name__ == "__main__":
    stockBuySell = StockBuySell()
    print(stockBuySell.stockBuySell([7,1,4,5,6,7,8,9,3,11]))