let app = new Vue({
	el: '#app',
	data: {
		str: '2022.04.04',
	},
	filters: {
		formatId: function(value) {
			return value + '.04.04.2002';
		}
	}
});