

let app = new Vue({
	el: '#app',
	data: {
    str: [
      new Date().getFullYear(),
      new Date().getMonth(),
      new Date().getDay(),
    ],
		
	},
	filters: {
		formatId: function(value) {
      const gg = value.reverse();
			return gg;
		}
	}
});
