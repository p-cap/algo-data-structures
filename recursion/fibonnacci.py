
def fib_rec(n):

    # Base case
    if n==0 or n==1:
        return n
    
    # Recursive case

    else:
        print(fib_rec(n-1))
        return fib_rec(n-1) + fib_rec(n-2)

fib_rec(4)