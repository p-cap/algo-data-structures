def reverse_sentence(sentence):

    #remove whitespaces and turn string into an array
    sentence_array = sentence.strip().split()

    sentence_array.reverse()

    final_string = " ".join(sentence_array)
    
    return final_string

def test(func, result):
    if func == result:
        print("Passed test")
    else:
        print("Failed test")

test(reverse_sentence('Hi John,   are you ready to go?'), 'go? to ready you are John, Hi')
test(reverse_sentence('    space before'), 'before space')
test(reverse_sentence('space after     '),'after space')
test(reverse_sentence('   Hello John    how are you   '),'you are how John Hello')
test(reverse_sentence('1'),'1')





