function getAvg(arr) { 
    let sum = 0;
    for (let elem of arr) { 
        sum += elem; 
    } 

    return sum / arr.length;
}

function getDivisors(num) {
    let result = [];

    for (let i = 2; i < num; i++) {
         if (num % i == 0) {
            result.push(i);
        } 
    }
        return result;
}
alert(getAvg(getDivisors(24)))