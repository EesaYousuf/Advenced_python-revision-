from functools import reduce

# Lambda for quick inline function
add = lambda a, b: a + b
print(add(3, 5))
# # Map
# nums = [1, 2, 3, 4]
# doubled = list(map(lambda x: x*2, nums))
# # Reduce (cumulative)
# product = reduce(lambda a, b: a*b, nums)

# print(doubled, evens, product) # type: ignore
from functools import reduce

nums = [1, 2, 3, 4]

doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))  # <- must be here
product = reduce(lambda a, b: a*b, nums)

print(doubled, evens, product)


