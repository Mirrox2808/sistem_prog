let arr = [1, 2, 3, 4, 5];
let sum = 0;

let res = arr.forEach(function(elem){
    sum += elem*elem;
});

console.log(sum);