characters = "theawesomeness"

console.log(myFunction(characters))

function myFunction(characters) {
    let mySet = new Set()

    for (i = 0; i < characters.length; i++) {
        if(mySet.size == 0) {
            mySet.add(characters.charAt[i])
        } else if (mySet.has(characters.charAt[i])) {
            return false
        }
    }
    return true
}

console.log(myFunction_v2(characters))

function myFunction_v2(characters) {

    let mySet = new Set(characters)

    return characters.length == mySet.length
}




