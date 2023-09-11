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