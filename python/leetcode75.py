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


# # # # # # # # # #
# 153. Find Minimum in Rotated Sorted Array - 7/75
# # # # # # # # # #

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         res = nums[0]
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             if nums[l] < nums[r]:
#                 res = min(res, nums[l])
#                 break

#             m = (l + r) // 2
#             res = min(res, nums[m])
#             if nums[m] >= nums[l]:
#                 l = m + 1
#             else:
#                 r = m - 1
#         return res
        
# print(Solution().findMin(nums = [3,4,5,1,2]))
# print(Solution().findMin(nums = [4,5,6,7,0,1,2]))
# print(Solution().findMin(nums = [11,13,15,17]))

# Time : O(log n)
# Memory : O(1)

# Example 1:

#     Input: nums = [3,4,5,1,2]
#     Output: 1
#     Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:

#     Input: nums = [4,5,6,7,0,1,2]
#     Output: 0
#     Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:

#     Input: nums = [11,13,15,17]
#     Output: 11
#     Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 


# # # # # # # # # #
# 33. Search in Rotated Sorted Array - 8/75
# # # # # # # # # #

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             mid = (l + r) // 2
#             if target == nums[mid]:
#                 return mid
            
#             # left sorted portion
#             if nums[l] <= nums[mid]:
#                 if target > nums[mid] or target < nums[l]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1

#             # right sorted portion
#             else:
#                 if target < nums[mid] or target > nums[r]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#         return -1

# print(Solution().search(nums = [4,5,6,7,0,1,2], target = 0))
# print(Solution().search(nums = [4,5,6,7,0,1,2], target = 3))
# print(Solution().search(nums = [1], target = 0))

# Example 1:

#     Input: nums = [4,5,6,7,0,1,2], target = 0
#     Output: 4

# Example 2:

#     Input: nums = [4,5,6,7,0,1,2], target = 3
#     Output: -1

# Example 3:

#     Input: nums = [1], target = 0
#     Output: -1


# # # # # # # # # #
# 15. 3Sum - 9/75
# # # # # # # # # #

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#         for i, a in enumerate(nums):
#             if i > 0 and a == nums[i - 1]:
#                 continue

#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1
#         return res
    
# print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))
# print(Solution().threeSum(nums = [0,1,1]))
# print(Solution().threeSum(nums = [0,0,0]))
    
# Example 1:

#     Input: nums = [-1,0,1,2,-1,-4]
#     Output: [[-1,-1,2],[-1,0,1]]
#     Explanation: 
#     nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#     nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#     nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#     The distinct triplets are [-1,0,1] and [-1,-1,2].
#     Notice that the order of the output and the order of the triplets does not matter.

# Example 2:

#     Input: nums = [0,1,1]
#     Output: []
#     Explanation: The only possible triplet does not sum up to 0.

# Example 3:

#     Input: nums = [0,0,0]
#     Output: [[0,0,0]]
#     Explanation: The only possible triplet sums up to 0.


# # # # # # # # # #
# 11. Container With Most Water - 10/75
# # # # # # # # # #

# class Solution:
#     def maxArea(self, height: List[int]) -> int:

        # # BRUTE FORCE
        # res = 0

        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)
        # return res
        
        
        # # LINEAR TIME SOLUTION
        # res = 0
        # l, r = 0, len(height) - 1

        # while l < r:
        #     area = (r - l) * min(height[l], height[r])
        #     res = max(res, area)

        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return res

# print(Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]))
# print(Solution().maxArea(height = [1,1]))

# Example 1:

#     Input: height = [1,8,6,2,5,4,8,3,7]
#     Output: 49
#     Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:

#     Input: height = [1,1]
#     Output: 1


# # # # # # # # # #
# 371. Sum of Two Integers - 11/75
# # # # # # # # # #

# class Solution:
#     def getSum(self, a: int, b: int) -> int:

#         bitShortener = 0xffffffff

#         while (b & bitShortener) > 0:
#             tmp = (a & b) << 1
#             a = (a ^ b)
#             b = tmp
            
#         return (a & bitShortener) if b > 0 else a
        

# print(Solution().getSum(a = 1, b = 2))
# print(Solution().getSum(a = 2, b = 3))
# print(Solution().getSum(a = -1, b = 1))

# Example 1:

#         Input: a = 1, b = 2
#         Output: 3

# Example 2:

#         Input: a = 2, b = 3
#         Output: 5

# Example 3:

#         Input: a = -1, b = 1
#         Output: 0


# # # # # # # # # #
# 191. Number of 1 Bits - 12/75
# # # # # # # # # #

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             n &= (n - 1)
#             res += 1
#         return res

# print(Solution().hammingWeight(n = 0o0000000000000000000000000001011))
# print(Solution().hammingWeight(n = 0o0000000000000000000000010000000))
# print(Solution().hammingWeight(n = 0o11111111111111111111111111111101))

# Example 1:

#         Input: n = 00000000000000000000000000001011
#         Output: 3
#         Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# Example 2:

#         Input: n = 00000000000000000000000010000000
#         Output: 1
#         Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

# Example 3:

#         Input: n = 11111111111111111111111111111101
#         Output: 31
#         Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
        

# # # # # # # # # #
# 338. Counting Bits - 13/75
# # # # # # # # # #

# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         dp = [0] * (n + 1)
#         offset = 1

#         for i in range(1, n + 1):
#             if offset * 2 == i:
#                 offset = i
#             dp[i] = 1 + dp[i - offset]

#         return dp

# print(Solution().countBits(n = 2))
# print(Solution().countBits(n = 5))

# Example 1:

#     Input: n = 2
#     Output: [0,1,1]
#     Explanation:
#     0 --> 0
#     1 --> 1
#     2 --> 10

# Example 2:

#     Input: n = 5
#     Output: [0,1,1,2,1,2]
#     Explanation:
#     0 --> 0
#     1 --> 1
#     2 --> 10
#     3 --> 11
#     4 --> 100
#     5 --> 101


# # # # # # # # # #
# 268. Missing Number - 14/75
# # # # # # # # # #

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res

print(Solution().missingNumber(nums = [3,0,1]))
print(Solution().missingNumber(nums = [0,1]))
print(Solution().missingNumber(nums = [9,6,4,2,3,5,7,0,1]))

# Example 1:

#     Input: nums = [3,0,1]
#     Output: 2
#     Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:

#     Input: nums = [0,1]
#     Output: 2
#     Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:

#     Input: nums = [9,6,4,2,3,5,7,0,1]
#     Output: 8
#     Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.