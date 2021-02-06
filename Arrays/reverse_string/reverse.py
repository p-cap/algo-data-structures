# method number one

def reverse_array(array):
    finalArray = []

    for i in range(len(sampleArray)):
        finalArray.append(sampleArray.pop())

    return finalArray

# method number two

def reverse_array_2(array):
    finalArray = []
    num = len(sampleArray) - 1

    for index, value in enumerate(sampleArray):
        finalArray.insert(index, sampleArray[num])
        num -= 1

    return finalArray

sampleArray = ["Pcap", "is", "Awesome"]


def reverse_array_3(array): 
    num = len(sampleArray) - 1
    Dict ={}

    for index, value in enumerate(sampleArray):
        Dict[num] = value
        num -= 1

    finalArray = []

    i = 0
    while i < len(sampleArray):
        print("This is i")
        for j in Dict:
            print("This is j")
            if i == j:
                finalArray.append(Dict[j])
                i += 1  

    return finalArray

print(reverse_array_3(sampleArray))

