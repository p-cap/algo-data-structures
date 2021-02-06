def recursion_sum(number):
    if number == 0:
        return 0
    else:
        return number + recursion_sum(number - 1)

if recursion_sum(4) == 10:
    print("recursion_sum is implemented correctly")

def sum_function(number):
    if number % 10 == 0:
        return number
    else:
        return number % 10 + sum_function(number // 10)

if sum_function(4321) == 10:
    print("sum_function is implemented correctly")



## I had to look this up

def word_split(phrase, words, output=None):

    if output is None:
        output = []
    
    for word in words:
        if phrase.startswith(word):
            output.append(word)

            return word_split(phrase[len(word):], words, output)
        
    return output

if word_split('themanran',['the','ran','man']) == ['the', 'man', 'ran']:
    print("Word_split was implemented correctly")
