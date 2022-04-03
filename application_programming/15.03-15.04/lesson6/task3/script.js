let app = new Vue({
	el: '#app',
	data: {
		items: [2,5,9,11,3],
	},
	methods: {
		removeItem: function(index) {
			this.items.splice(index, 1);
		}
	}
});