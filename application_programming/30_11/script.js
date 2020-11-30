function but(){
    /*txt.value = 'Привет';
    txta.value = 'Hello';
    let mass = [
        function(){ return 'Karina'},
        function() {return 'Leonid'},
        function(){return 'Andrei'},
        function(){return 'Vlad'}
    ];

    txt.value = mass[1]();

    for(let elem of mass) {
        txta.value += elem()+'\n';

    }

    let obj = {
        key1: function(){ return 'Karina'},
        key2: function() {return 'Leonid'}
    };

    txt.value = obj.key2();

    txta.value +='\nОбъект \n';

    for(let key in obj) {
        txta.value += obj[key]()+'\n';
    }
*/
    let arr=[
        function(){return 1;},
        function(){return 2;},
        function(){return 3;} ]
        txt.value = (arr[2]());
        txta.value = (arr[0]()+arr[1]()+arr[2]());

        for(let elem of arr){ alert (elem()) }

}