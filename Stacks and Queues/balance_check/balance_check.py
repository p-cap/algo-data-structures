# reference: https://digitalu.udemy.com/course/python-for-data-structures-algorithms-and-interviews/learn/lecture/3179634?start=300#overview


def balance_check(object):

    if len(object)%2 != 0:
        return False

    # creating our openning brackets
    openning = set('([{')

    # creating tuples for the mathing below
    matches = set([('(',')'),('[',']'),('{','}')])

    stack = []

    for parenthesis in object:
        if parenthesis in openning:
            stack.append(parenthesis)
                
        else:

            # this validates if the very first element in the stack is an openning bracket
            if len(stack) == 0:
                return False


            last_open = stack.pop()

            # last_open will always be an open bracket
            # in other words, anything in the stack are opening brackets
            if(last_open, parenthesis) not in matches:
                return False

    return len(stack) == 0



print(balance_check('[]'))
# print(balance_check('[](){([[[]]])}'))
# print(balance_check('()(){]}'))


matches = set([('(',')'),('[',']'),('{','}')])



