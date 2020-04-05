import timeit

# def fact(n):
#     """calculate n! iteratively """
#     result = 1
#     if n > 1:
#         for f in range(2, n + 1):
#             result *= f
#     return result
#
# for i in range(130):
#     print(i, fact(i))
#
#
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)

def fib(n):
    """ F(n) = F(n-1)+F(n-2) """
    if n<2:
        return n
    else:
        return fib(n-1)  +fib(n-2)


for i in range(36):
     print(i, fib(i))

print (timeit.timeit(fib(n)),1)
