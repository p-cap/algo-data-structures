def compress(string):   
    Dict = {}
    temp = ""

    if string == '':
        return "\'\'"

    for i in string:
        if temp == i:
            value = Dict[i] + 1
            Dict[i] = value
            temp = i
        else:
            Dict[i] = 1
            temp = i

    new = ""
    for index in Dict:
        new += index
        new += str(Dict[index])

    return new

print(compress("AAAAABBBBB"))
print(compress(''))
print(compress('AABBCC'))
print(compress('AAABCCDDDDD'))







