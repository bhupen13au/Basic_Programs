# # Fibonacci without Memoization
# def fibo(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibo(n-1) + fibo(n-2)
#
# for i in range(1,101):
#     print(fibo(i))


# # Fibonacci with cache logic
# cache = {}
# def fibo(n):
#     if n in cache:
#         return cache[n]
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         value = fibo(n-1) + fibo(n-2)
#         cache[n] = value
#         return value
#
# for i in range(1,501):
#     print(fibo(i))


# # Fibonacci with Memoization
# from functools import lru_cache
#
# @lru_cache(maxsize=1000)
# def fibo(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibo(n-1) + fibo(n-2)
#
# for i in range(1,901):
#     print(fibo(i))