def sample_recursion(i):    
    # print("main")
    # base case 
    if i == 0 or i == 1:
        # print("IF :" + str(i))
        return i

    # calling other functions to determine the 
    # sequence on how the recursive function is being called
    else:
        # print(f1(i - 1))
        return f1(i - 1) + f2(i - 2)

def f1(j):
    # print("I'm f1")
    # print("f1:" + str(j))
    return sample_recursion(j)

def f2(k):
    # print("I'm f2")
    # print("f2:" + str(k))
    return sample_recursion(k)

# print("Result:" + str(sample_recursion(4)))


# testing retrun termination

def ret(b):
    for i in range(b):
        return ret(b)
    


# return does not comply with a for loop even though 
# the return is inside a loop
