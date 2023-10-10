from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP



print(Solution().maxProfit(prices=[7,1,5,3,6,4]))
print(Solution().maxProfit(prices=[7,6,4,3,1]))
print(Solution().maxProfit(prices=[3,7,1,4]))