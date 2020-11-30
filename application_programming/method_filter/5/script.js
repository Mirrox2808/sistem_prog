let arr = [2,-3,150,254,15,1,10];

let res = arr.filter(function(elem,index){
    if (elem*index < 30){return true;}
    else{return false;}
});

console.log(res);