# # # # # # # # # #
# VARIABLES
# # # # # # # # # #

# # Variables are given their type dynamically
# n = 0
# print('n =', n)
# # result is
# # n = 0

# # changed type from int to str
# n = "abc"
# print('n =', n)
# # result is
# # n = abc

# # Multiple assignments
# n, m = 0, "abc"
# print('n =', n, 'm =', m)
# # result is
# # n = 0 m = abc

# n, m, z = 0.125, "abc", False
# print('n =', n, 'm =', m, 'z =', z)
# # result is
# # n = 0.125 m = abc z = false

# # Increment
# n = n + 1 # good
# n += 1    # good
# # n++       # bad

# # None is null (absence of value)
# n = 4
# n = None
# print("n =", n)
# # result is
# # n = None


# # # # # # # # # #
# IF-STATEMENTS
# # # # # # # # # #

# # If statements don't need parentheses or curly braces
# n = 1
# if n > 2:
#     n -= 1
# elif n == 2:
#     n *= 2
# else:
#     n += 2
# print('n =', n)
# # result is
# # n = 3

# # Parentheses needed for multi-line conditions
# #  and = &&
# # or   = ||
# n, m = 1, 2
# if((n > 2 and
#     n != m) or n == m):
#     n += 1
# print('n =', n, 'm =', m)
# # result is 
# # n = 1 m = 2


# # # # # # # # # #
# LOOPS
# # # # # # # # # #

# n = 0
# while n < 5:
#     print(n)
#     n += 1
# # result is
# # 0
# # 1
# # 2
# # 3
# # 4

# # Looping from i = 0 to i = 4
# for i in range(5):
#     print(i)
# # result is
# # 0
# # 1
# # 2
# # 3
# # 4

# # Looping from i = 2 to i = 5
# for i in range(2, 6):
#     print(i)
# # result is
# # 2
# # 3
# # 4
# # 5

# # Looping from i = 5 to i = 2
# for i in range(5, 1, -1):
#     print(i)
# # result is
# # 5
# # 4
# # 3
# # 2


# # # # # # # # # #
# MATH
# # # # # # # # # #

# # Division is decimal by default
# print(5 / 2)
# # result is
# # 2.5

# # Double slash rounds down
# print(5 // 2)
# # result is
# # 2

# # CAREFUL: most languages round towards 0 by default
# # So negative numbers will round down
# print(-3 // 2)
# # result is
# # -2

# # A workaround for rounding towards zero
# # is to use decimal division and then convert to int.
# print(int(-3 / 2))
# # result is
# # -1

# # Modding is similar to most languages
# print(10 % 3)
# # result is
# # 1

# # Except for negative values
# print(-10 % 3)
# # result is
# # 2

# # To be consistent with other languages modulo
# import math
# from multiprocessing import heap
# print(math.fmod(-10, 3))
# # result is
# # -1.0

# # More math helpers
# import math
# print(math.floor(3 / 2))
# # result is
# # 1
# print(math.ceil(3 / 2))
# # result is
# # 2
# print(math.sqrt(2))
# # result is
# # 1.4142135623730951
# print(math.pow(2, 3))
# # result is
# # 8

# # Max / Min Int
# # float("inf") is used as upper value for comparison to find lowest values
# # float("-inf") is used as lower value for comparison to find largest values
# #
# highest_path_cost = float("-inf")
# lowest_path_cost = float('inf')
# # pretend that these were calculated using some worthwhile algorithm
# path_costs = [1, 100, 2000000000000, 50]
# for path in path_costs:
#     if path < lowest_path_cost:
#         lowest_path_cost = path
# #
# for path in path_costs:
#     if path > highest_path_cost:
#         highest_path_cost = path
# #
# print(lowest_path_cost, highest_path_cost)
# # result is
# # 1 2000000000000


# # Python numbers are infinite so they never overflow
# import math
# print(math.pow(2, 200))
# # result is
# # 1.6069380442589903e+60

# # But still less than infinity
# import math
# print(math.pow(2, 200) < float("inf"))
# # result is
# # True


# # # # # # # # # #
# ARRAYS
# # # # # # # # # #

# # Arrays (called lists in python)
# arr = [1, 2, 3]
# print(arr)
# # result is
# # [1, 2, 3]

# # Can be used as a stack
# arr.append(4)
# arr.append(5)
# print(arr)
# # result is
# # [1, 2, 3, 4, 5]

# arr.pop()
# print(arr)
# # result is
# # [1, 2, 3, 4]

# arr.insert(1, 7)
# print(arr)
# # result is
# # [1, 7, 2, 3, 4]

# arr[0] = 0
# arr[3] = 0
# print(arr)
# # result is
# # [0, 7, 2, 0, 4]

# # Initialize arr of size n with default value of 1
# n = 5
# arr = [1] * n
# print(arr)
# print(len(arr))
# # result is
# # [1, 1, 1, 1, 1]
# # 5

# # Careful: -1 is not out of bounds, it's the last value
# arr = [1, 2, 3]
# print(arr[-1])
# # result is
# # 3

# # Indexing -2 is the second to last value, etc.
# print(arr[-2])
# # result is
# # 2

# # Sublists (aka slicing)
# arr = [1, 2, 3, 4]
# print(arr[1:3])
# # result is
# # [2, 3]

# # Similar to for-loop ranges, last index is non-inclusive
# print(arr[0:4])
# # result is
# # [1, 2, 3, 4]

# # But no out of bounds error
# print(arr[0:10])
# # result is
# # [1, 2, 3, 4]

# # Unpacking
# a, b, c = [1, 2, 3]
# print(a, b, c)
# # result is
# # 1 2 3

# # Be careful though
# a, b = [1, 2, 3]
# print(a)
# # result is
# # ValueError: too many values to unpack (expected 2)

# # Loop through arrays
# nums = [1, 2, 3]

# # Using index
# for i in range(len(nums)):
#     print(nums[i])
# # result is
# # 1
# # 2
# # 3

# # Without index
# for n in nums:
#     print(n)
# # result is
# # 1
# # 2
# # 3

# # With index and value
# for i, n in enumerate(nums):
#     print(i, n)
# # result is
# # 0 1
# # 1 2
# # 2 3

# # Loop through multiple arrays simultaneously with unpacking
# nums1 = [1, 3, 5]
# nums2 = [2, 4, 6]
# for n1, n2 in zip(nums1, nums2):
#     print(n1, n2)
# # result is
# # 1 2
# # 3 4
# # 5 6

# # Reverse
# nums = [1, 2, 3]
# nums.reverse()
# print(nums)
# # result is
# # [3, 2, 1]

# # Sorting
# arr = [5, 4, 7, 3, 8]
# arr.sort()
# print(arr)
# # result is
# [3, 4, 5, 7, 8]

# arr.sort(reverse=True)
# print(arr)
# # result is
# [8, 7, 5, 4, 3]

# arr = ["bob", "alice", "jane", "doe"]
# arr.sort()
# print(arr)
# # result is
# # ['alice', 'bob', 'doe', 'jane']

# # Custom sort (by length of string)
# arr.sort(key=lambda x: len(x))
# print(arr)
# # result is
# # ['bob', 'doe', 'jane', 'alice']

# # List comprehension
# arr = [i for i in range(5)]
# print(arr)
# # result is
# # [0, 1, 2, 3, 4]

# # 2-D lists
# arr = [[0] * 4 for i in range(4)]
# print(arr)
# print(arr[0][0], arr[3][3])
# # result is
# # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# # 0 0 this is printing the first and last zero of the line

# # This won't work
# # arr = [[0] * 4] * 4

# # # # # # # # # #
# STRINGS
# # # # # # # # # #

# # Strings are similar to arrays
# s = "abc"
# print(s[0:2])
# # result is
# # ab

# # But they are immutable
# s[0] = "A"
# print(s[0])
# # result is
# # TypeError: 'str' object does not support item assignment

# # So this creates a new string
# s += "def"
# print(s)
# # result is
# # abcdef

# # Valid numeric strings can be converted
# print(int("123") + int("123"))
# # result is
# # 246

# # And numbers can be converted to strings
# print(str(123) + str(123))
# # result is
# # 123123

# # In rare cases you may need the ASCII value of a char
# print(ord("a"))
# print(ord("b"))
# # result is
# # 97
# # 98

# # Combine a list of strings (with an empty string delimitor)
# strings = ["ab", "cd", "ef"]
# print("".join(strings))
# # result is
# # abcdef