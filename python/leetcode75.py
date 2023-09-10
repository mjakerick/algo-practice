# # # # # # # # # #
# TWO SUM
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

# # Time : O(n^2)
# # Memory : O(1) because it doesn't use additional memory that depends on the input size

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

# # Time : O(n)
# # Memory : O(n)

# # Example 1:

# #     Input: nums = [2,7,11,15], target = 9
# #     Output: [0,1]
# #     Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# # Example 2:

# #     Input: nums = [3,2,4], target = 6
# #     Output: [1,2]

# # Example 3:

# #     Input: nums = [3,3], target = 6
# #     Output: [0,1]