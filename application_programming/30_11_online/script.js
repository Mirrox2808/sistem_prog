function but(){
    /*txt.value = 'Привет';
    txta.value = 'Hello';*/
    let mass = [
        function(){return 1},
        function(){return 2},
        function(){return 3}
    ];

    let sum = 0;
    for(let elem of mass) {
        sum += elem();
    }
    txt.value=sum;
/*
    let obj = {
        key1: function(){ return 'Karina'},
        key2: function() {return 'Leonid'}
    };

    txt.value = obj.key2();

    txta.value +='\nОбъект \n';

    for(let key in obj) {
        txta.value += obj[key]()+'\n';

    }*/
}