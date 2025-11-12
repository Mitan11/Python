# Empty tuple
t0 = ()
print(t0, type(t0))  # () <class 'tuple'>

# Single-element tuple (note the trailing comma)
t1 = (1,)
print(t1)  # (1,)

# Without parentheses (tuple packing)
t2 = 1, 2, 3
print(t2)  # (1, 2, 3)

# With parentheses
t3 = (1, 2, 3)
print(t3)  # (1, 2, 3)

# From an iterable
t4 = tuple([1, 2, 3])
print(t4)  # (1, 2, 3)

# Mixed types and nested structures
t5 = (1, "a", 3.14, [4, 5], (6, 7))
print(t5)  # (1, 'a', 3.14, [4, 5], (6, 7))

# The tuple is immutable, but items inside it can be mutable:
t = (1, [2, 3])
# t[0] = 99  # TypeError: 'tuple' object does not support item assignment
t[1].append(4)      # OK: modifies the inner list, not the tuple
print(t)            # (1, [2, 3, 4])
#assigning values to tuple elements is not allowed
t += (5,)  # Creates a new tuple; original t remains unchanged
print(t)   # (1, [2, 3, 4], 5)

t = ('a', 'b', 'c', 'd', 'e')

print(t[0])    # 'a'
print(t[-1])   # 'e'
print(t[1:4])  # ('b', 'c', 'd')
print(t[:3])   # ('a', 'b', 'c')
print(t[::2])  # ('a', 'c', 'e')

print('c' in t)     # True
for item in t:
    print(item, end=' ')  # a b c d e
print()

# Basic unpacking
a, b, c = (10, 20, 30)
print(a, b, c)  # 10 20 30

# Swapping variables
x, y = 1, 2
x, y = y, x
print(x, y)  # 2 1

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)  # 1 [2, 3, 4] 5

# Tuple operations
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)   # (1, 2, 3, 4)
print(t1 * 3)    # (1, 2, 1, 2, 1, 2)

nums = (5, 2, 9, 1)

print(len(nums))      # 4
print(min(nums))      # 1
print(max(nums))      # 9
print(sum(nums))      # 17

# sorted() returns a list; original tuple remains unchanged
print(sorted(nums))   # [1, 2, 5, 9]
print(nums)           # (5, 2, 9, 1)

print((1, 2, 3) < (1, 2, 4))    # True
print((2, 0) > (1, 99))         # True

t = ('a', 'b', 'a', 'c', 'a')

print(t.count('a'))     # 3
print(t.index('b'))     # 1
# print(t.index('z'))   # ValueError if element not found

t = (3, 1, 4, 1, 5)

print(len(t))          # 5
print(sum(t))          # 14
print(min(t), max(t))  # 1 5
print(sorted(t))       # [1, 1, 3, 4, 5]
print(tuple('abc'))    # ('a', 'b', 'c')

# enumerate returns (index, value) tuples
for i, v in enumerate(('x', 'y', 'z'), start=1):
    print(i, v)  # 1 x ; 2 y ; 3 z

# zip creates tuples element-wise from iterables
names = ('Alice', 'Bob', 'Charlie')
ages = (25, 30, 35)
paired = tuple(zip(names, ages))
print(paired)  # (('Alice', 25), ('Bob', 30), ('Charlie', 35))