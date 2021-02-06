
function continuousSum(array) {

    max_sum = current_sum = array[0] 
    
    for (num = 1; num < array.length; num++) {

        current_sum = Math.max(current_sum+array[num], array[num])    

        max_sum = Math.max(max_sum, current_sum)
    }

    return max_sum
}

console.log(continuousSum([1,2,-1,3,4,10,10,-10,-1]))
