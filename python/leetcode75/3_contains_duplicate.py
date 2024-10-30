from typing import List

# # # # # # # # # #
# 217. Contains Duplicate - 3/75
# # # # # # # # # #

# Brute Force
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
    
print(Solution().containsDuplicate(nums = [1,2,3,1]))
print(Solution().containsDuplicate(nums=[1,2,3,4]))
print(Solution().containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))

# Time : O(n^2)
# Memory : O(1)


# Sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
print(Solution().containsDuplicate(nums = [1,2,3,1]))
print(Solution().containsDuplicate(nums=[1,2,3,4]))
print(Solution().containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))

# Time : O(nlogn)
# Memory : O(1)


# Hash Set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
print(Solution().containsDuplicate(nums = [1,2,3,1]))
print(Solution().containsDuplicate(nums=[1,2,3,4]))
print(Solution().containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))

# Time : O(n)
# Memory : O(n)


# Hash Map
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False
    
print(Solution().containsDuplicate(nums = [1,2,3,1]))
print(Solution().containsDuplicate(nums=[1,2,3,4]))
print(Solution().containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))

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