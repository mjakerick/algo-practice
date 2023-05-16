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