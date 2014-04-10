function Repositories(endpoint) {

	this.server = endpoint;

	this.get = function() {
		console.log("Get from endpoint");
	};

	this.render = function() {
		console.log("Rendering repositories");
	};

}

function Issues(endpoint) {
	this.server = endpoint;

	this.get = function() {
		console.log("Get from issues");
	};

	this.render = function() {
		console.log("Rendering issues");
	};
}

var wallet = {

	endpoint: 'http://localhost:8000', 
	repositories: new Repositories(this.endpoint),
	issues: new Issues(this.endpoint),

	init: function() {
		console.log("wallet app started");
		this.repositories.get();
	}

};

wallet.init();