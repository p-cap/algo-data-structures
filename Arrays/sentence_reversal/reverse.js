sampleInput = [
    'Hi John,   are you ready to go?',
    '    space before',
    'space after     ',
    '   Hello John    how are you   ',
    '1'
].forEach((input) => {
    
    // replace function replaces the extra spaces with single spaces
    // the trim function removes trailing and beginning spaces
    input = input.replace(/\s\s+/g, " ").trim()

    //turns the string into an array with a " " as the delimiter
    input = input.split(" ")

    // reverses the array
    input.reverse()

    // join converts the array back into a string with a space delimiter
    reversed = input.join(" ")
    console.log(reversed)
})




