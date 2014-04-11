function Repositories(endpoint) {

	this.get = function() {
		$.getJSON('repositories/', this.render);
	};

	this.render = function(obj) {
		var el = $('#repo-line').html(); 
		var temp = '';
		for (var r in obj) {
			temp += _.template(el, {repo : obj[r]});
		}
		$('#repositories').html(temp);
		console.log("Repositories Rendered");
	};
}

function Issues() {

	this.get = function() {
		console.log("Get from issues");
	};

	this.render = function() {
		console.log("Rendering issues");
	};
}

function Propositions() {

	this.get = function() {
		console.log("Get from propositions");
	};

	this.create = function() {

	};

	this.render = function() {
		console.log("Rendering propositions");
	};
};

var wallet = {

	repositories: new Repositories(),
	issues: new Issues(),

	init: function() {
		console.log("wallet app started");
	},

	getRepositories: function() {
		this.repositories.get();
	},
};

$(document).ready(function() {
	wallet.init();
	wallet.getRepositories();
});
