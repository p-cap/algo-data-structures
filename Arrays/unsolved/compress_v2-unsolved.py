# def compress(string):

#     finalString = ""

#     if string == "":
#         return "\"\""

#     if len(string) == 1:
#         return finalString + 1

#     count = 1
#     i = 1

#     for letter in string:
#         if letter == string[i - 1]:
#             # finalString = finalString + letter + str(count + 1)
#             i += 1
#             count += 1
#         else:
#             finalString += finalString + letter + str(count)
#             count = 1
#             i += 1
    
#     return finalString

# print(compress('AAAAABBBBCCCC'))


# The script below will let me understand negative indexes
# the for loop will terminate if the next character is DIFFERENT

# count = 0
# index = 0
# for i in string:
#     if string[index - 1] == string[index - 2]:
#         print(string[index - 1])
#         index -= 1
        
#     else:
#         print("A different letter is encountered")
#         print("The letter is " + string[index - 2])
#         break

string = 'AAAAABBBBCCCC'




index = 1


for letter in string:
    
    def inner(index):
        count = 0
        finalString = ""    
        print(count)
        print(index)
        if letter == string[index]:
            print(letter)
            # if IndexError:
            #     break
            # # finalString = finalString + letter + str(count + 1)
            # else: 
            #     continue
            count += 1
            index += 1
            return
        else:
            finalString = finalString + letter + str(count)
            count = 1
            index += 1
            return
    inner(index)




