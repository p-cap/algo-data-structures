factorial_memo = {}

factorial_memo[0] = 0

def factorial(k):

    if k < 2:
        return 1
    
    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    
    print(factorial_memo)
    return factorial_memo[k]

print(factorial(4))
    
