from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

print(Solution().twoSum(nums = [3,4,5,6], target = 7))
print(Solution().twoSum(nums = [4,5,6], target = 10))
print(Solution().twoSum(nums = [5,5], target = 10))