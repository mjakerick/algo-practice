# # Variables are given their type dynamically
# n = 0
# print('n =', n)

# # changed type from int to str
# n = "abc"
# print('n =', n)


# # Multiple assignments
# n, m = 0, "abc"
# print('n =', n, 'm =', m)

# n, m, z = 0.125, "abc", False
# print('n =', n, 'm =', m, 'z =', z)

# # Increment
# n = n + 1 # good
# n += 1    # good
# # n++       # bad

# # None is null (absence of value)
# n = 4
# n = None
# print("n =", n)

# # If statements don't need parentheses or curly braces
# n = 1
# if n > 2:
#     n -= 1
# elif n == 2:
#     n *= 2
# else:
#     n += 2
# print('n =', n)

# # Parentheses needed for multi-line conditions
# #  and = &&
# # or   = ||
# n, m = 1, 2
# if((n > 2 and
#     n != m) or n == m):
#     n += 1
# print('n =', n, 'm =', m)