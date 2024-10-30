from typing import List

# # # # # # # # # #
# 121. Best Time to Buy and Sell Stock - 2/75
# # # # # # # # # #

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left = buy, right = sell
        maxP = 0

        while r < len(prices):
            # profitable?
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

# Time : O(n)
# Memory : O(1)

# Example 1:

#     Input: prices = [7,1,5,3,6,4]
#     Output: 5
#     Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#     Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

#     Input: prices = [7,6,4,3,1]
#     Output: 0
#     Explanation: In this case, no transactions are done and the max profit = 0.