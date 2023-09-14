from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# # # # # # # # # #
# 1. TWO SUM - 1/75
# # # # # # # # # #

# # Brute Force : Nested For Loops
# class Solution:
#     def twoSum(self, nums: [int], target: int) -> [int]:
#         for i, a in enumerate(nums):
#             for j, b in enumerate(nums[i+1:]):
#                 if a+b==target:
#                     return [i, j+i+1]

# print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
# print(Solution().twoSum(nums=[2, 7, 11, 15], target=18))
# print(Solution().twoSum(nums=[2, 7, 11, 15], target=22))

# Time : O(n^2)
# Memory : O(1) because it doesn't use additional memory that depends on the input size

# # Clever Solution : Hash Map
# class Solution:
#     def twoSum(self, nums: [int], target: int) -> [int]:
#         prevMap = {} # val : index

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i
#         return
    
# print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
# print(Solution().twoSum(nums=[2, 7, 11, 15], target=18))
# print(Solution().twoSum(nums=[2, 7, 11, 15], target=22))

# Time : O(n)
# Memory : O(n)

# Example 1:

#     Input: nums = [2,7,11,15], target = 9
#     Output: [0,1]
#     Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

#     Input: nums = [3,2,4], target = 6
#     Output: [1,2]

# Example 3:

#     Input: nums = [3,3], target = 6
#     Output: [0,1]


# # # # # # # # # #
# 121. Best Time to Buy and Sell Stock - 2/75
# # # # # # # # # #

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l, r = 0, 1 # left = buy, right = sell
#         maxP = 0

#         while r < len(prices):
#             # profitable?
#             if prices[l] < prices[r]:
#                 profit = prices[r] - prices[l]
#                 maxP = max(maxP, profit)
#             else:
#                 l = r
#             r += 1

#         return maxP
    
# print(Solution().maxProfit(prices=[7,1,5,3,6,4]))
# print(Solution().maxProfit(prices=[7,6,4,3,1]))

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


# # # # # # # # # #
# 217. Contains Duplicate - 3/75
# # # # # # # # # #

# # Brute Force
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         n = len(nums)
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
    
# print(Solution().containsDuplicate(nums = [1,2,3,1]))
# print(Solution().containsDuplicate(nums=[1,2,3,4]))
# print(Solution().containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))

# Time : O(n^2)
# Memory : O(1)


# # Sorting
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         n = len(nums)
#         for i in range(1, n):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False
    
# print(Solution().containsDuplicate(nums = [1,2,3,1]))
# print(Solution().containsDuplicate(nums=[1,2,3,4]))
# print(Solution().containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))

# Time : O(nlogn)
# Memory : O(1)


# # Hash Set
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()

#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False
    
# print(Solution().containsDuplicate(nums = [1,2,3,1]))
# print(Solution().containsDuplicate(nums=[1,2,3,4]))
# print(Solution().containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))

# Time : O(n)
# Memory : O(n)


# # Hash Map
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = {}
#         for num in nums:
#             if num in seen and seen[num] >= 1:
#                 return True
#             seen[num] = seen.get(num, 0) + 1
#         return False
    
# print(Solution().containsDuplicate(nums = [1,2,3,1]))
# print(Solution().containsDuplicate(nums=[1,2,3,4]))
# print(Solution().containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))

# Time : O(n)
# Memory : O(n)

# Example 1:

#     Input: nums = [1,2,3,1]
#     Output: true

# Example 2:

#     Input: nums = [1,2,3,4]
#     Output: false

# Example 3:

#     Input: nums = [1,1,1,3,3,4,3,2,4,2]
#     Output: true


# # # # # # # # # #
# 238. Product of Array Except Self - 4/75
# # # # # # # # # #

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1] * (len(nums))

#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res

# print(Solution().productExceptSelf(nums = [1,2,3,4]))
# print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))

# Time : O(n)
# Memory : O(n)

# Example 1:

#     Input: nums = [1,2,3,4]
#     Output: [24,12,8,6]

# Example 2:

#     Input: nums = [-1,1,0,-3,3]
#     Output: [0,0,9,0,0]


# # # # # # # # # #
# 53. Maximum Subarray - 5/75
# # # # # # # # # #

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSub = nums[0]
#         curSum = 0

#         for n in nums:
#             if curSum < 0:
#                 curSum = 0
#             curSum += n
#             maxSub = max(maxSub, curSum)
#         return maxSub

# print(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
# print(Solution().maxSubArray(nums = [1]))
# print(Solution().maxSubArray(nums = [5,4,-1,7,8]))

# Time : O(n)
# Memory : O(1)

# Example 1:

#     Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#     Output: 6
#     Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:

#     Input: nums = [1]
#     Output: 1
#     Explanation: The subarray [1] has the largest sum 1.

# Example 3:

#     Input: nums = [5,4,-1,7,8]
#     Output: 23
#     Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# # # # # # # # # #
# 152. Maximum Product Subarray - 6/75
# # # # # # # # # #

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         res = max(nums)
#         curMin, curMax = 1, 1

#         for n in nums:
#             if n == 0:
#                 curMin, curMax = 1, 1
#                 continue
            
#             tmp = curMax * n
#             curMax = max(n * curMax, n * curMin, n)
#             curMin = min(tmp, n * curMin, n)
#             res = max(res, curMax, curMin)
#         return res

# print(Solution().maxProduct(nums = [2,3,-2,4]))
# print(Solution().maxProduct(nums = [-2,0,-1]))

# Time : O(n)
# Memory : O(1)

# Example 1:

#     Input: nums = [2,3,-2,4]
#     Output: 6
#     Explanation: [2,3] has the largest product 6.

# Example 2:

#     Input: nums = [-2,0,-1]
#     Output: 0
#     Explanation: The result cannot be 2, because [-2,-1] is not a subarray.