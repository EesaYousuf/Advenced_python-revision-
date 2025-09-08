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
