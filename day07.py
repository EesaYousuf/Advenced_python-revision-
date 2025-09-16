from functools import reduce

# Lambda for quick inline function
add = lambda a, b: a + b
print(add(3, 5))
# Map
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, nums))

