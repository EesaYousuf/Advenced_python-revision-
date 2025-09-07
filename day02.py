# Iterator Example
nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2
# Generator Example
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for val in countdown(5):
    print(val)


