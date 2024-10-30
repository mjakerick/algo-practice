from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range (n - 1):
            for j in range (i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

print(Solution().hasDuplicate(nums = [1,2,3,1]))
print(Solution().hasDuplicate(nums=[1,2,3,4]))
print(Solution().hasDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))