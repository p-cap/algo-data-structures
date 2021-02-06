# treat each element as an output

def permutation(s):
    
    output = []

    # base case
    if len(s) == 1:
        output = [s]

    else:
        # for every in string 

        for i, letter in enumerate(s):
            
            # for every permutation
            for perm in permutation( s[:1] + s[i+1:]):
                output += [letter + perm]

    return output

s = 'def'

print(permutation(s))



