# Fibonacci with Memoization (recursion + dictionary cache)
# Advanced recursion with memoization
fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    if n <= 1:
        value = n
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    fib_cache[n] = value
    return value

print([fibonacci(i) for i in range(15)])
# Functions and 
# Map, Filter, Reduce example
from functools import reduce

nums = [5, 10, 15, 20, 25]

squared = list(map(lambda x: x**2, nums))
even = list(filter(lambda x: x % 2 == 0, nums))
sum_all = reduce(lambda a, b: a + b, nums)

print("Squared:", squared)
print("Even:", even)
print("Sum:", sum_all)


