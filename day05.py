def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def prime_check(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))
