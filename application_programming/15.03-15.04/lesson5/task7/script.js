let app = new Vue({
	el: '#app',
	data: {
		items: [1,5,-2,-5,9,11,3],
	},
	methods: {
		filter: function() {
			this.items = this.items.filter(function(elem){
				if (elem < 10 && elem >0){
					return elem;
				}
			});
		},
	},
});