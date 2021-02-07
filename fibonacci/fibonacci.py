# my iterative solution
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

# solutions from: Jose Portilla's course

# iterative approach

def fib_iterative(n):

  # set a starting point
  a, b = 0,1 

  print("#######################")
  print("Visualization Data Flow")

  print("a Initial value: " + str(a))
  print("b Initial value: " + str(b))

  for i in range(n):
    temp = b
    print("########################\u2193")
    a,b = b,a+b 
    print("a = b: " + str(a) + " <------------- " + str(temp))
    print("b = a + b: " + str(b) + " ->--------\u27DE")
  return str(a) + " <---------------------\u2193"

print(fib_iterative(4))


# recursive version

