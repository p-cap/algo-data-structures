def fib(n):

    # base case
    if n == 1:
      return 0
   
    elif n == 2 or n == 3:
      return 1

    sum = 0
    first = 0
    second = 1
   
    for i in range(n - 2):
        sum = first + second
        first = second
        second = sum
   
    return sum

# test if the fibonacci code is correct
fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fib(10) == fibonacci_sequence[10 - 1])

