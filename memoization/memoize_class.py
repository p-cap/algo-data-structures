class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    # __call__ allows the class to called like a function
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
    
def factorial(k):
    if k < 2:
        return 1
    
    return k * factorial(k - 1)

factorial = Memoize(factorial)

factorial(4)



