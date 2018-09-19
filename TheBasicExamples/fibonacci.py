import time
def fibonacci(i):

    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci(i - 1) + fibonacci(i - 2)


memo = {}
def fibonacci_memoize(i):
    if i in memo:
        return memo[i]
    if i == 0:
        return 0
    if i == 1:
        return 1
    fib_num = fibonacci_memoize(i - 1) + fibonacci_memoize(i - 2)
    memo[i] = fib_num
    return fib_num


t_start = time.time()
print(fibonacci_memoize(33))

print('time elapsed ', time.time() - t_start)
