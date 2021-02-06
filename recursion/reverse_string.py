# only use recursion

def reverse(word):
    
    # base case 
    if len(word) == 1:
        return word

    # recursion

    return reverse(word[1:]) + word[0] 

print(reverse("abc"))







