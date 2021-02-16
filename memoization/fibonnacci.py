# n = 10
# cache = [None]*(n+1)

# print(cache)
# print("Object type: " + str(type(cache)))
# print(len(cache))


# Instantiate Cache information
n = 3
cache = [None] * (n + 1)


def fib_dyn(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Check cache
    if cache[n] != None:
        return cache[n]
    
    # Keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    print("first:" + str(fib_dyn(n-1)))
    print("second: " +str(fib_dyn(n-2)))
    print(cache)
    return cache[n]

print("Results: " + str(fib_dyn(n)))